import readchar

def main():
    while True:
        key = readchar.readchar()
        print(f'Tecla presionada: {key}')
        if key == '\x1b[A':  # Código de escape para la tecla de flecha hacia arriba
            print('Tecla ↑ presionada. Saliendo del bucle.')
            break

if __name__ == "__main__":
    main()
