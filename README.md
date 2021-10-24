# MitMirror

[Configurando o ambiente para rodar o Projeto](project_setup.md).


Projeto de site com funções de To-Do list e características de rede social.
O projeto esta sendo desenvolvido em *Python*, utilizando o micro-framework *Flask* e *MySQL* como Banco de Dados.
![Tela Inicial do Site](https://user-images.githubusercontent.com/76628101/131269909-6d24fb2a-b359-4e05-a16f-9358b8689580.png)
---

## Register e Login:

A função de Register recebe os dados enviados pelo usuário, faz a validação de que o usuário realmente completou os campos que são requiridos e que a confirmação de senha digitada é igual a senha.
O sistema também compara os dados digitados com os dados de usuários ja cadastrados no banco de dados para identificar se ja existe alguem aquele email ou nome de usuário, em caso positivo emite um aviso, pedindo para que o usuário digite dados diferentes.
O sistema de armazenamento de senhas, utiliza uma criptografia para que seja preservada a segurança do usuário, a senha é criptografada com um hash antes de ser armazenada no banco de dados.
![Tela de Register](https://user-images.githubusercontent.com/76628101/131269926-7193df03-efce-4dfe-889b-089066616813.png)

A função de Login recebe os dados enviados pelo usuário, compara com os dados do banco de dados, e efetua o login caso o usuário ja esteja cadastrado, em caso negativo apenas emite um aviso indicando que o nome de usuário ou senha esta inválido.
![Tela de Login](https://user-images.githubusercontent.com/76628101/131269921-7d292e37-8009-4a42-bcae-2c92a424cf24.png)

Assim que o usuário cadastrado efetua o login, é direcionado para o seu perfil, (página que ainda está em desenvolvimento), onde ele podera ver algumas informações, editar alguns dados, manipular suas listas de afazeres e objetivos, além de poder interagir com amigos que também estejam utilizando a aplicação.
![perfil](https://user-images.githubusercontent.com/76628101/131374718-79194f13-23a2-4241-8233-a1c74bd54476.png)




O projeto esta caminhando aos poucos, e inicialmente tem objetivos acadêmicos, focando principalmente no back-end, a parte de front-end é temporária e vai melhorar futuramente, creio que é melhor explorar uma coisa de cada vez para absorver o conhecimento e aprendizado.
