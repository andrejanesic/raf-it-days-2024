from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

sys_prompt = """\
Ti si koristan i ljubazan asistent koji pomaže kupcima da se snađu na \
onlajn prodavnici biciklističke opreme. Ukoliko ne znaš da daš tačan \
odgovor, odgovori korisniku da nemaš dovoljno informacija i nikako ne \
pokušavaj da smisliš odgovor. Tvoji odgovori moraju biti informativni \
i da tačno odgovore na korisničko pitanje. Moraš detaljno da odgovoriš \
na pitanje, tvoj odgovor mora imati bar dve rečenice. Na svako pitanje \
moraš ponuditi dodatnu pomoć klijentu, baš kao jedan pravi prodavac. A \
ako kupac nema više pitanja, onda moraš predložiti kupcu da završi sa \
kupovinom odabranih proizvoda. Kupovina proizvoda se vrši na linku:
#kupiSada?sviProizvodi
"""

memory = ChatMemoryBuffer.from_defaults(token_limit=6_000)

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=sys_prompt,
    llm=llm,
    verbose=True,
)


def chatbot(message, _):
    # response = chat_engine.chat(message)
    # return str(response)
    res = ""
    response = chat_engine.stream_chat(message)
    for token in response.response_gen:
        res += str(token)
        yield(res)
    return res

demo = gr.ChatInterface(
    fn=chatbot,
    textbox=gr.Textbox(placeholder="Pitaj me sve o našim biciklima", container=False, scale=7),
    title="MojBajs - Prodaja",
    description="Pomoć u odabiru bicikla i biciklističke opreme.",
    theme="soft",
    clear_btn=None,
    undo_btn=None,
    retry_btn=None,
).queue(default_concurrency_limit=5)

demo.launch()
