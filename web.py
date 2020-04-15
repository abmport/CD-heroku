import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tudo sobre Google Glass</title>
    <link rel="stylesheet" href="./_css/estilo.css" />
    <script language="javascript" src="./_javascript/funcoes.js"></script>
</head>

<body>

    <div id="interface">
        <header id="cabecalho">
            <hgroup>
                <h1>Google Glass</h1>
                <h2>A revolução do Google está chegando</h2>
            </hgroup>

            <img id="icone" src="_imagens/glass-oculos-preto-peq.png" alt="Oculos Google Glass">
            <nav id="menu">
                <h1>Menu Principal</h1>
                <ul>
                    <li onmousemove="trocaLogo('_imagens/home.png')"
                        onmouseout="trocaLogo('_imagens/glass-oculos-preto-peq.png')"><a href="index.html">Home</a></li>
                    <li onmousemove="trocaLogo('_imagens/especificacoes.png')"
                        onmouseout="trocaLogo('_imagens/glass-oculos-preto-peq.png')"><a href="#">Especificações</a>
                    </li>
                    <li onmousemove="trocaLogo('_imagens/fotos.png')"
                        onmouseout="trocaLogo('_imagens/glass-oculos-preto-peq.png')"><a href="#">Fotos</a></li>
                    <li onmousemove="trocaLogo('_imagens/multimidia.png')"
                        onmouseout="trocaLogo('_imagens/glass-oculos-preto-peq.png')"><a href="#">Multimídia</a></li>
                    <li onmousemove="trocaLogo('_imagens/contato.png')"
                        onmouseout="trocaLogo('_imagens/glass-oculos-preto-peq.png')"><a href="fale-conosco.html">Fale
                            conosco</a></li>
                </ul>
            </nav>
        </header>
        <section id="corpo">
            <article id="noticia-principal">
                <header id="cabecalho-artigo">
                    <hgroup>
                        <h3>Tecnologia > Inovações</h3>
                        <h1>Saiba tudo sobre o Google Glass</h1>
                        <h2>por Gustavo Guanabara</h2>
                        <h3 class="direita">Atualizado em 23/Abril/2013</h3>
                    </hgroup>
                </header>
                <h2>O que é</h2>
                <p>O <b> Google Glass</b> é um acessório em forma de óculos que possibilita a interação dos usuários com
                    diversos conteúdos em realidade aumentada. Também chamado de <i>Project Glass</i>, o eletrônico é
                    capaz de tirar fotos a partir de comandos de voz, enviar mensagens instantâneas e realizar
                    vídeoconferências. Seu lançamento está previsto para 2014, e seu preço deve ser de US$ 1,5 mil.
                    Atualmente o <em>Google Glass</em> encontra-se em fase de testes e já possui um vídeo totalmente
                    gravado com o dispositivo. Além disso, a companhia de buscas registrou novas patentes anti-furto e
                    de desbloqueio de tela para o acessório.</p>

                <figure class="foto-legenda">
                    <img src="_imagens/glass-quadro-homem-mulher.jpg" alt="homem mulher usando oculos">
                    <figcaption>
                        <h3>Google glass</h3>
                        <p>uma nova maneira de ver o mundo</p>
                    </figcaption>
                </figure>

                <h2>Data de lançamento</h2>
                <p>Não há uma data específica e oficial para o dispositivo ser lançado, ainda. Pode ser que ele esteja
                    disponível em demonstrações a partir de 2013, mas seu lançamento para as lojas fica para, pelo
                    menos, 2014.</p>

                <h2>Especificações Técnicas</h2>
                Tabela Técnica do Google Glass Mar/2013

                Tabela Técnica do Google Glass Mar/2013

                Tela:Resolução equivalente a tela de 25"
                Camera: 5MP para fotos / 720p para vídeos
                Conectividade: Wi-Fi/ Bluetooth
                Memória Interna: 12GB

                <h2>Como funciona</h2>
                <p>De acordo com fontes próximas do Google, os óculos vão contar com uma pequena tela de LCD ou AMOLED
                    na parte superior e em frente aos olhos do usuário. Com o uso de uma câmera e GPS, você pode se
                    situar, assim como selecionar opções com o movimento da cabeça</p>

                <h2>O que você pode fazer com o Google Glasses</h2>
                <p>O vídeo de divulgação do Google mostra que você pode se transformar em uma espécie de “super-humano”,
                    já que o aparelho pode indicar a quantos metros você está de seu destino, se o metrô está aberto ou
                    fechado, mostrar o clima, agenda e até mesmo permitir que você marque encontros apenas com comandos
                    de voz.</p>

                <figure>
                    <img src="_imagens/video-mini01.jpg" alt="homem mulher usando oculos">
                    <figcaption>


            </article>
        </section>
        <aside id="lateral">
            <h1>Outras Notícias</h1>
            <h2>Vídeo mais recente</h2>

            <img src="./_imagens/video-mini02.jpg" alt="Videos Propaganda">

            <h2>Novidades no Glass</h2>
            <p>O Google enfim revelou as especificações completas do Google Glass, e com ele uma surpresa ainda inédita
                no mercado: a gigante das buscas usará um sistema de áudio baseado na transdução por condução. Através
                das hastes dos óculos, o som será transmitido para o ouvido do usuário por meio de microvibrações em
                determinados ossos de sua cabeça, sem usar nenhum tipo de alto-falante.</p>

            <p>Além da surpresa do áudio, a tela montada a frente do olho do usuário também chamou atenção. Serão 640 x
                360 pixels de resolução que, em proporção, equivaleria a um monitor de 25 polegadas de alta definição
                colocado a 2,5 metros de distância do espectador.</p>
        </aside>
        <footer id="rodape">
            <p>Copyright &copy; 2013 - by Gustavo Guanabara <br>
                <a href="http://facebook.com/cursosemvideo" target="_blank"> Facebook</a>
                |
                <a href="http://twitter.com/cursosemvideo" target="_blank">Twitter</a></p>
        </footer>
    </div>
</body>

</html>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
