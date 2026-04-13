from abc import ABC, abstractmethod

class VectorStore(ABC):
    """
    Abstrct contract: any vector BD must implement these methods.
    """
    @abstractmethod
    def add_documents(self, docs: list[str]) -> None:
        """Add documents to the store"""
        pass

    @abstractmethod
    def similarity_search(self, query: str, k: int = 5) -> list[str]:
        """Find k most similarity documents."""
        pass

    def search_and_formate(self, query: str) -> str:

        pass

class PineconeStore(VectorStore):
    def add_documents(self, docs: list[str]) -> None:
        print(f"Adding {len(docs)} docs to pinecone")

    def similarity_search(self, query: str, k: int = 5) -> list[str]:
        return [f"Pinecone result {i}" for i in range(k)]
    

class chromaStore(VectorStore):
    def add_documents(self, docs: list[str]) -> None:
        print(f"Adding {len(docs)} docs to Chroma")

    def similarity_search(self, query: str, k: int = 5) -> list[str]:
        return [f"Chroma result {i}" for i in range(k)]
    

