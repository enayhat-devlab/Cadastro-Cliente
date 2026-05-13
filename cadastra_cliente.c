// ---------------- CLIENTE ----------------
void cadastrar_cliente(descritor_cli *d) {
    nocliente *novo = (nocliente*) malloc(sizeof(nocliente));

    printf("Nome: ");
    scanf(" %[^\n]", novo->dado_cli.nome);

    printf("Email: ");
    scanf(" %[^\n]", novo->dado_cli.email);

    novo->prox_cli = d->iniciocliente;
    d->iniciocliente = novo;
    d->quantcliente++;

    printf("Cliente cadastrado!\n");
}

