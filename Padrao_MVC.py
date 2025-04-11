# Modelo (Model)
class Book:
    def __init__(self, titulo: str, autor: str, ano: str):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"


# Visão (View)
class View:
    def show_menu(self) -> int:
        print("\nMenu:")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Remover Livro")
        print("4 - Sair")
        return int(input("Escolha uma opção: "))

    def get_book(self) -> Book:
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        return Book(titulo, autor, ano)

    def show_books(self, books: list):
        if not books:
            print("Nenhum livro cadastrado.")
        else:
            print("\nLista de Livros:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")

    def show_message(self, message: str):
        print(f"\n{message}")


# Controlador (Controller)
class Controller:
    def __init__(self):
        self.books = []
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.list_books()
            elif choice == 3:
                self.remove_book()
            elif choice == 4:
                self.view.show_message("Saindo do sistema...")
                break
            else:
                self.view.show_message("Opção inválida! Tente novamente.")

    def add_book(self):
        book = self.view.get_book()
        self.books.append(book)
        self.view.show_message("Livro cadastrado com sucesso!")

    def list_books(self):
        self.view.show_books(self.books)

    def remove_book(self):
        self.list_books()
        index = int(input("\nDigite o número do livro a remover: ")) - 1
        if 0 <= index < len(self.books):
            removed_book = self.books.pop(index)
            self.view.show_message(f"Livro '{removed_book.titulo}' removido com sucesso!")
        else:
            self.view.show_message("Número inválido!")

# Executar o programa
if __name__ == "__main__":
    controller = Controller()
    controller.run()
