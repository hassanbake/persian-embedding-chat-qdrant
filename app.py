import environments
from dotenv import load_dotenv

from langchain_community.vectorstores import Qdrant
from langchain.text_splitter import CharacterTextSplitter

def read_text_from_file(file_path):
    text = ""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    return text_splitter.split_text(text)

def main():
    load_dotenv()

    text = read_text_from_file("sample-fa.txt")
    chunks = get_chunks(text)

    # a = environments.OPENAI_API_KEY

if __name__ == "__main__":
    main()