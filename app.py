import sys
import configparser
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox, QTextEdit, QVBoxLayout, QWidget, QGroupBox, QFileDialog, QComboBox, QTextBrowser
from PyQt6.QtCore import pyqtSignal, QObject, QThread, Qt
import random
import time
import instagrapi
from datetime import datetime, timedelta
from instagrapi import Client
from instagrapi.exceptions import FeedbackRequired

# Sinal personalizado para atualizar a GUI a partir de threads
class SinalLog(QObject):
    anexar_log = pyqtSignal(str)

class AplicativoBotInstagram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sinal_log = SinalLog()
        self.setWindowTitle("InstaBot")
        self.setFixedSize(250, 700)
        self.running_label = None 
        self.initUI()
        self.ini_file_path = os.path.join(os.getcwd(), f"{self.username_input.text()}.ini")

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Nome de usuário
        username_label = QLabel("Nome de Usuário do Instagram:", central_widget)
        main_layout.addWidget(username_label)
        self.username_input = QLineEdit(central_widget)
        main_layout.addWidget(self.username_input)

        # Senha
        password_label = QLabel("Senha do Instagram:", central_widget)
        main_layout.addWidget(password_label)
        self.password_input = QLineEdit(central_widget)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(self.password_input)

        # Porcentagens de Engajamento
        grupo_porcentagem = QGroupBox("Porcentagens de Engajamento", central_widget)
        layout_porcentagem = QVBoxLayout()  # Initialize the layout first
        layout_porcentagem.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Then set the alignment

        # Porcentagem de Comentários
        porcentagem_comentarios_label = QLabel("Porcentagem de Comentários:", grupo_porcentagem)
        layout_porcentagem.addWidget(porcentagem_comentarios_label)
        self.porcentagem_comentarios_spinbox = QSpinBox(grupo_porcentagem)
        self.porcentagem_comentarios_spinbox.setRange(0, 100)
        layout_porcentagem.addWidget(self.porcentagem_comentarios_spinbox)

        # Porcentagem de Seguidores
        porcentagem_seguir_label = QLabel("Porcentagem de Seguir:", grupo_porcentagem)
        layout_porcentagem.addWidget(porcentagem_seguir_label)
        self.porcentagem_seguir_spinbox = QSpinBox(grupo_porcentagem)
        self.porcentagem_seguir_spinbox.setRange(0, 100)
        layout_porcentagem.addWidget(self.porcentagem_seguir_spinbox)

        # Taxa Mínima de Engajamento
        taxa_engajamento_label = QLabel("Taxa Mínima de Engajamento (%):", grupo_porcentagem)
        layout_porcentagem.addWidget(taxa_engajamento_label)
        self.taxa_engajamento_spinbox = QSpinBox(grupo_porcentagem)
        self.taxa_engajamento_spinbox.setRange(0, 100)  # Ajuste o limite conforme necessário
        layout_porcentagem.addWidget(self.taxa_engajamento_spinbox)
        grupo_porcentagem.setLayout(layout_porcentagem)
        main_layout.addWidget(grupo_porcentagem)
        
        # Comentários
        self.checkbox_comentarios = QCheckBox("Habilitar Comentários", central_widget)
        main_layout.addWidget(self.checkbox_comentarios)
        label_lista_comentarios = QLabel("Lista de Comentários:", central_widget)
        main_layout.addWidget(label_lista_comentarios)
        self.textedit_lista_comentarios = QTextEdit(central_widget)
        main_layout.addWidget(self.textedit_lista_comentarios)
        botao_adicionar_comentario = QPushButton("Adicionar Comentário", central_widget)
        main_layout.addWidget(botao_adicionar_comentario)
        botao_adicionar_comentario.clicked.connect(self.adicionar_comentario)

        # Localização
        label_localizacao = QLabel("Selecionar Localização:", central_widget)
        main_layout.addWidget(label_localizacao)
        self.combobox_localizacao = QComboBox(central_widget)
        self.preencher_combobox_localizacao()
        main_layout.addWidget(self.combobox_localizacao)

        # Mensagem de execução do Bot
        self.running_label = QLabel("", self) 
        self.running_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.running_label) 

        # Botão Iniciar
        self.botao_iniciar = QPushButton("Iniciar Bot", central_widget)
        main_layout.addWidget(self.botao_iniciar)
        self.botao_iniciar.clicked.connect(self.iniciar_bot)

        # Botão Exibir Log
        botao_exibir_log = QPushButton("Exibir Log da Aplicação", central_widget)
        main_layout.addWidget(botao_exibir_log)
        botao_exibir_log.clicked.connect(self.exibir_log)

        # Definir Layout
        central_widget.setLayout(main_layout)
        self.janela_log = QTextBrowser()  # Janela para exibir logs
        self.janela_log.setWindowTitle("Log da Aplicação")
        self.janela_log.setGeometry(100, 100, 600, 400)

        # Conectar sinais para atualizar o log na GUI
        self.sinal_log.anexar_log.connect(self.janela_log.append)

        # Validar campos sempre que o texto for alterado
        self.username_input.textChanged.connect(self.validar_campos)
        self.password_input.textChanged.connect(self.validar_campos)
        self.textedit_lista_comentarios.textChanged.connect(self.validar_campos)

    def adicionar_comentario(self):
        arquivo_comentario, ok = QFileDialog.getOpenFileName(self, "Selecionar Arquivo de Comentário", "", "Arquivos de Texto (*.txt);;Todos os Arquivos (*)")
        if ok:
            with open(arquivo_comentario, "r") as arquivo:
                texto_comentario = arquivo.read()
                texto_atual = self.textedit_lista_comentarios.toPlainText()
                if texto_atual:
                    texto_atual += "\n" + texto_comentario
                else:
                    texto_atual = texto_comentario
                self.textedit_lista_comentarios.setPlainText(texto_atual)

    def preencher_combobox_localizacao(self):
        try:
            with open("locations.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    partes = linha.strip().split(":")
                    if len(partes) == 2:
                        nome_localizacao, codigo_localizacao = partes
                        self.combobox_localizacao.addItem(nome_localizacao)
        except FileNotFoundError:
            self.sinal_log.anexar_log.emit("Arquivo 'locations.txt' não encontrado.")

    def validar_campos(self):
        nome_usuario = self.username_input.text()
        senha = self.password_input.text()
        porcentagem_comentarios = self.porcentagem_comentarios_spinbox.value()
        porcentagem_seguir = self.porcentagem_seguir_spinbox.value()
        comentarios_habilitados = self.checkbox_comentarios.isChecked()
        lista_comentarios = self.textedit_lista_comentarios.toPlainText()

        if nome_usuario and senha and (porcentagem_comentarios >= 0) and (porcentagem_seguir >= 0) and (comentarios_habilitados or lista_comentarios):
            self.botao_iniciar.setEnabled(True)
        else:
            self.botao_iniciar.setEnabled(False)

    def iniciar_bot(self):
        # Cria uma nova thread para executar o bot
        self.bot_thread = QThread()
        self.bot_thread.run = self.executar_bot
        self.bot_thread.start()
        if self.running_label is not None:
            self.running_label.setText("Executando o bot...")

    def executar_bot(self):
        self.sinal_log.anexar_log.emit("InstaBot Versão 1.0")
        self.sinal_log.anexar_log.emit("Bot iniciado.")

        # Inicializar instância do Cliente do instagrapi
        cl = Client()

        # Tenta fazer login com tratamento de exceções
        try:
            cl.login(self.username_input.text(), self.password_input.text())
            self.sinal_log.anexar_log.emit(f"Login realizado na conta {self.username_input.text()}\n")
        except instagrapi.exceptions.BadPassword:
            self.sinal_log.anexar_log.emit("Senha incorreta. Por favor, tente novamente.")
            return
        except Exception as e:
            self.sinal_log.anexar_log.emit(f"Erro ao fazer login: {e}")
            return

        # Lê códigos de localização do arquivo locations.txt
        nome_localizacao_selecionada = self.combobox_localizacao.currentText()
        codigo_localizacao_selecionada = self.obter_codigo_localizacao(nome_localizacao_selecionada)

        # Lista de comentários a ser usada pelo bot
        comentarios = self.textedit_lista_comentarios.toPlainText().splitlines()

        # Configurações de interação
        porcentagem_comentarios = self.porcentagem_comentarios_spinbox.value()
        porcentagem_seguir = self.porcentagem_seguir_spinbox.value()
        taxa_minima_engajamento = self.taxa_engajamento_spinbox.value()

        # Usuários que não devem ser seguidos ou interagidos
        usuarios_desabilitados = []

        # Caminho para o arquivo .ini
        self.ini_file_path = f"{self.username_input.text()}.ini"
        usuarios_interagidos = set()
        config = configparser.ConfigParser()
        if os.path.exists(self.ini_file_path):
            config.read(self.ini_file_path)
            if 'Interacted_Users' in config:
                usuarios_interagidos = set(config['Interacted_Users'])

        # Configurações de filtro de usuários
        MIN_SEGUINDO = 200
        MAX_SEGUIDORES = 200000
        MAX_SEGUINDO = 200000

        # Definir tempo de execução para 1 hora a partir de agora
        end_time = datetime.now() + timedelta(hours=1)

        # Definir momento para a próxima pausa
        proximo_tempo_pausa = datetime.now() + timedelta(minutes=4)

        # Funções auxiliares
        def deve_comentar():
            return random.randint(1, 100) <= porcentagem_comentarios

        def deve_seguir():
            return random.randint(1, 100) <= porcentagem_seguir

        def pausa_humana():
            tempo_de_espera = random.uniform(8, 16)
            self.sinal_log.anexar_log.emit(f"\nAguardando {tempo_de_espera:.2f} segundos antes da próxima ação.")
            time.sleep(tempo_de_espera)

        def fazer_uma_pausa():
            self.sinal_log.anexar_log.emit("\nIniciando uma pausa de 1:30 minutos.")
            time.sleep(90)

        def usuário_atende_critérios(informações_usuario, cl):
            # Definir a quantidade de postagens recentes para calcular o engajamento
            quantidade_postagens_recentes = 10
            postagens_recentes = cl.user_medias(informações_usuario.pk, amount=quantidade_postagens_recentes)

            # Se o usuário não tiver postagens suficientes, use a quantidade que ele tem
            quantidade_postagens_atual = min(len(postagens_recentes), quantidade_postagens_recentes)

            # Calcular total de curtidas e comentários em postagens recentes
            total_curtidas = sum(media.like_count for media in postagens_recentes[:quantidade_postagens_atual])
            total_comentarios = sum(media.comment_count for media in postagens_recentes[:quantidade_postagens_atual])

            # Calcular taxa de engajamento
            if quantidade_postagens_atual > 0 and informações_usuario.follower_count > 0:
                taxa_engajamento = ((total_curtidas + total_comentarios) / (informações_usuario.follower_count * quantidade_postagens_atual)) * 100
            else:
                taxa_engajamento = 0

            # Obter data da última postagem
            ultima_data_postagem = postagens_recentes[0].taken_at if postagens_recentes else None

            # Aplicar filtros avançados
            critérios_atendidos = (
                informações_usuario.follower_count <= MAX_SEGUIDORES and
                informações_usuario.following_count >= MIN_SEGUINDO and
                informações_usuario.following_count <= MAX_SEGUINDO and
                taxa_engajamento >= taxa_minima_engajamento
            )

            if not critérios_atendidos:
                # Se o usuário não atende aos critérios, pula para o próximo usuário
                self.sinal_log.anexar_log.emit(f"\nUsuário {informações_usuario.username} não atendeu à taxa mínima de engajamento, pulando...")
                return False, taxa_engajamento, ultima_data_postagem
            return True, taxa_engajamento, ultima_data_postagem

        def interagir_com_localizacao(codigo_localizacao, recente=True):
            nonlocal proximo_tempo_pausa
            nome_localizacao = self.combobox_localizacao.currentText()  # Obter o nome da localização atualmente selecionada
            self.sinal_log.anexar_log.emit(f"Procurando publicações pela localização de {nome_localizacao}")
            publicacoes = (cl.location_medias_recent if recente else cl.location_medias_top)(codigo_localizacao, amount=50)
            for publicacao in publicacoes:
                interacao_feita = False
                try:
                    id_usuario = publicacao.user.pk
                    if publicacao.user.username not in usuarios_desabilitados and id_usuario not in usuarios_interagidos:
                        informacoes_usuario = cl.user_info(id_usuario)
                        criterios_atendidos, taxa_engajamento, ultima_data_postagem = usuário_atende_critérios(informacoes_usuario, cl)
                        if criterios_atendidos:
                            self.sinal_log.anexar_log.emit(
                                f"\nTaxa de engajamento do usuário {publicacao.user.username} é de {round(taxa_engajamento)}%, "
                                f"e sua última postagem foi em {ultima_data_postagem.strftime('%d/%m/%Y')}"
                            )
                            cl.media_like(publicacao.id)
                            self.sinal_log.anexar_log.emit(f"Curtiu a publicação de {publicacao.user.username}.")
                            usuarios_interagidos.add(str(id_usuario)) 
                            interacao_feita = True
                            save_interacted_users()

                            if deve_seguir():
                                cl.user_follow(id_usuario)
                                self.sinal_log.anexar_log.emit(f"Seguindo {publicacao.user.username}.")

                            if not publicacao.comments_disabled and deve_comentar():
                                comentario = random.choice(comentarios)
                                cl.media_comment(publicacao.id, comentario)
                                self.sinal_log.anexar_log.emit(f"Comentando '{comentario}' na publicação de {publicacao.user.username}.")

                        # Se uma interação foi feita, esperar entre 8 e 16 segundos
                        if interacao_feita:
                            pausa_humana()
                        else:
                            self.sinal_log.anexar_log.emit(f"Nenhuma nova interação com {publicacao.user.username}, avançando imediatamente...")

                        if datetime.now() >= proximo_tempo_pausa:
                            fazer_uma_pausa()
                            proximo_tempo_pausa = datetime.now() + timedelta(minutes=30)

                except instagrapi.exceptions.MediaUnavailable:
                    self.sinal_log.anexar_log.emit("Erro: A publicação foi deletada e não está mais disponível.")
                except Exception as e:
                    self.sinal_log.anexar_log.emit(f"Erro inesperado: {e}")

        def save_interacted_users():
            config = configparser.ConfigParser()

            # Carrega arquivo .ini existente, se houver
            if os.path.exists(self.ini_file_path):
                config.read(self.ini_file_path)

            # Adiciona seção e usuários interagidos ao arquivo .ini
            if 'Interacted_Users' not in config.sections():
                config.add_section('Interacted_Users')

            for usuario in usuarios_interagidos:
                config.set('Interacted_Users', usuario, 'True')

            # Escreve as alterações no arquivo .ini
            with open(self.ini_file_path, 'w') as arquivo_config:
                config.write(arquivo_config)

        # Loop principal
        while datetime.now() < end_time:
            recente = True 
            interagir_com_localizacao(codigo_localizacao_selecionada, recente)
            recente = not recente
            if datetime.now() >= end_time:
                break

        save_interacted_users()  # Salva usuários interagidos no final da execução
        self.sinal_log.anexar_log.emit("O script atingiu o tempo de execução definido. Encerrando...")
        cl.logout()

    def obter_codigo_localizacao(self, nome_localizacao):
        try:
            with open("locations.txt", "r") as arquivo:
                for linha in arquivo:
                    nome, codigo = linha.strip().split(':')
                    if nome == nome_localizacao:
                        return codigo
        except FileNotFoundError:
            self.sinal_log.anexar_log.emit("Arquivo 'locations.txt' não encontrado.")
        return None

    def exibir_log(self):
        self.janela_log.show()

def principal():
    app = QApplication(sys.argv)
    janela = AplicativoBotInstagram()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    principal()
