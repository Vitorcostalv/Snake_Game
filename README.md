# Snake_Game


Optei por fazer um estudo pessoal sobre o uso do `curses` porque sempre fui fascinado por jogos clássicos e interfaces minimalistas que funcionam diretamente no terminal. Há algo especial em criar algo funcional e visual usando apenas caracteres e coordenadas, sem depender de ferramentas modernas ou gráficos avançados. Além de ser um desafio técnico, é uma forma de me conectar com a simplicidade e a criatividade que marcaram os primeiros passos do desenvolvimento de jogos.

O `curses` funciona manipulando diretamente o que aparece na tela do terminal, usando coordenadas (linhas e colunas) para posicionar elementos como texto e símbolos. É como desenhar em um quadro invisível, atualizando cada detalhe manualmente. Essa abordagem me ensinou a pensar de forma estruturada, planejando cada movimento, cada atualização, como se estivesse construindo uma obra pixel por pixel.

Escolhi recriar o jogo da cobrinha porque ele é um clássico atemporal, simples de entender, mas com desafios interessantes de lógica e programação. Foi uma oportunidade de aprender mais sobre manipulação de eventos (como detectar teclas pressionadas), lógica de colisões, e como tornar a experiência fluida mesmo em um ambiente tão restrito. 

Este projeto me mostrou como desenvolvedores do passado transformavam limitações em inovação. Trabalhar no terminal me fez valorizar a engenhosidade necessária para criar algo visual e interativo com tão poucos recursos. É um lembrete poderoso de que grandes ideias não dependem de ferramentas sofisticadas, mas sim de criatividade e dedicação.

Esplicação rapida porque da primeira vez não rodou

Para rodar um programa que usa o módulo `curses` no Windows, você precisa de uma solução alternativa, pois o Python padrão para Windows não inclui suporte nativo ao `curses`. Felizmente, existe um pacote chamado `windows-curses`, que resolve essa limitação. Aqui está o passo a passo para instalá-lo e utilizá-lo:

---

### **1. Verifique se o Python e o pip estão instalados**
Antes de instalar o `windows-curses`, certifique-se de que o Python e o gerenciador de pacotes `pip` estão configurados corretamente no seu sistema.

- No terminal ou prompt de comando, execute:
  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```
  Isso deve retornar a versão do Python instalada. Caso não esteja instalado, você pode baixá-lo em [python.org](https://www.python.org/).

- Para confirmar que o `pip` está funcionando, digite:
  ```bash
  pip --version
  ```

---

### **2. Instale o `windows-curses`**
O pacote `windows-curses` é essencial para rodar programas que usam `curses` no Windows. Para instalá-lo:

1. Abra o prompt de comando ou terminal.
2. Execute:
   ```bash
   pip install windows-curses
   ```

Se tudo estiver correto, você verá uma mensagem indicando que o pacote foi instalado com sucesso.

---

### **3. Teste seu programa**
Após a instalação, o módulo `curses` estará disponível no Windows. Agora você pode executar seu script Python que usa `curses` diretamente no terminal.

Para testar:
1. Navegue até o diretório onde está o arquivo `.py` do seu programa:
   ```bash
   cd caminho/do/seu/programa
   ```
2. Execute:
   ```bash
   python nome_do_seu_arquivo.py
   ```

---

### **4. Solução de problemas comuns**
- **Erro: `pip` não é reconhecido**:
  Certifique-se de que o Python está adicionado ao PATH. Você pode corrigir isso durante a instalação do Python, marcando a opção "Add Python to PATH".
  
- **Problema ao instalar o `windows-curses`**:
  Verifique se o Python que você está usando é de 32 ou 64 bits, e instale a versão do pacote compatível.

---


