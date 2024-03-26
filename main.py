from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer
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
moraš da započneš odgovor sa "Drago mi je da Vam pomognem!" ili sličnim \
pozdravom od poštovanja. Svako pitanje moraš da završiš sa "Da li bih \
mogao još nekako da Vam pomognem?" a ako kupac nema više pitanja, onda \
moraš predložiti kupcu da završi sa kupovinom odabranih proizvoda.
"""

memory = ChatMemoryBuffer.from_defaults(token_limit=6_000)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=sys_prompt,
    verbose=True,
)

response = chat_engine.chat("Koje bicikle nudi prodavnica za gradsku upotrebu?")
print(response)