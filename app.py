Segue o passo a passo completo pra mandar pro Mateus:

1. Logar no Graph Explorer

Abrir developer.microsoft.com/graph/graph-explorer
Clicar no ícone de pessoa (canto superior direito) e logar com uma conta que tenha papel de Administrador Global (ou Administrador de Aplicativo) no tenant da Lucralize.

2. Pegar o site-id

Método: GET
URL: https://graph.microsoft.com/v1.0/sites/lucralize.sharepoint.com
Clicar em "Run query"
No resultado (Response preview), copiar o valor do campo "id" — vai ser algo como lucralize.sharepoint.com,xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx,xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

3. Autorizar o app nesse site

Trocar o método de GET pra POST
URL: https://graph.microsoft.com/v1.0/sites/{cole aqui o id do passo 2}/permissions
Clicar na aba "Request Body" e colar:
json
{
  "roles": ["write"],
  "grantedToIdentities": [
    {
      "application": {
        "id": "c0868f3b-764c-4c5b-a9fc-4af4b6eb0baf",
        "displayName": "lucralize-gestao-comercial"
      }
    }
  ]
}
Clicar em "Run query"

4. Confirmar que funcionou

Resposta esperada: status 201, com um "id" de permissão novo no corpo da resposta.
Se der erro de permissão insuficiente, confirma que a conta logada no passo 1 é mesmo admin do tenant.

Pede pra ele mandar o print da resposta do passo 3, que eu confiro se ficou certo.
