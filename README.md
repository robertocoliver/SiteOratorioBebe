# SiteOratorioBebe
Modelo de site utilizado para construir uma aplicação web de uma escola de comunidade. Este é um trabalho voluntário e sem fins lucrativos.
#

 Criar um banco de dados no MariaDB ou MySQL

```bash
  sudo service mysql start
```
Acesse o console do MariaDB
```bash
  mysql -u root -p
```
Criar um banco de dados
```bash
  CREATE DATABASE nome_do_banco_de_dados;
```
Escolhendo o banco de dados
```bash
  use nome_do_banco_de_dados;
```
Criando um usuário e senha
```bash
  CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
```
Conceder todos os privilégios ao usuário no banco de dados 
```bash
  GRANT ALL PRIVILEGES ON oratorio.* TO 'seu_usuario'@'localhost';
```
Alterar as configurações no arquivo config.py
```bash
  class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://seu_usuario:sua_senha@localhost/seu_banco_de_dados'
```

 Reiniciar o serviço do MariaDB 
 ```bash
  service mysql restart
```

