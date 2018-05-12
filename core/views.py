from django.shortcuts import render

def cadastro_disciplina(request):
    contexto = {
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cadastro_disciplina.html", contexto)


def cursos(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
        "cursos":[
            {"nome":"Redes de Computadores", "link":"/cursos/desc-redes/"},
            {"nome":"Análise e Desenvolvimento de Sistemas", "link":"/cursos/desc-ads/"}, 
            {"nome":"Banco de Dados", "link":"/cursos/desc-bd/"}
        ]
    }
    return render(request, "cursos.html", contexto)


def desc_ads(request):
    contexto={
        "titulo":"Descrição de Curso Análise e Desenvolvimento de Sistemas",
        "descricao":"Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados. O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação.",
        "perfil":"O aluno que escolhe estudar Análise e Desenvolvimento de Sistemas é apaixonado por tecnologia e deseja transformar o futuro. Ele está sempre antenado nos avanços tecnológicos e nas novas ferramentas e gadgets. Além disso, possui raciocínio lógico e tem interesse em aprender a criar aplicativos para celulares e desenvolver programas para empresas.",
        "mercado":"A área de Análise e Desenvolvimento de Sistemas está entre as que mais contratam no País. Empresas públicas ou privadas de TI, de telecomunicações, entre outros segmentos, são opções com oportunidades atraentes para este profissional. Você pode atuar como Analista de Requisitos, Analista de Desenvolvimento, Analista de Sistemas, Analista de Negócio e Analista de Teste ou ainda desenvolver aplicativos para celular ou jogos para computador."
        }
    return render(request, "descricaocursos.html", contexto)


def desc_bd(request):
    contexto={
        "titulo":"Descrição de Curso Banco de Dados",
        "descricao": "O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas de desenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área. A graduação mostra a importância da segurança de compartilhamento de dados nas empresas modernas e ensina as melhores técnicas e ferramentas de criação e implementação da mesma. Na Impacta, você será preparado para o cenário real de gestão e liderança empresarial, garantindo a capacidade de comunicação e criatividade para solucionar problemas, atingir os melhores resultados, aumentar a produtividade e reduzir custos.",
        "perfil": "O curso é ideal tanto para quem deseja atuar na área de administração e gerenciamento de Banco de Dados quanto para quem já atua e quer ter uma formação superior na área, buscando mais conhecimento para aprimoramento e crescimento no setor. Para que seja bem-sucedido em sua área de atuação, o aluno deverá possuir algumas características pessoais importantes, tais como: capacidade de análise, organização, facilidade com cálculos matemáticos, dinamismo, habilidade para trabalhos em equipe e resoluções de problemas.",
        "mercado": "Um profissional em Banco de Dados recém-formado vai encontrar um mercado totalmente voltado para a tecnologia, com ferramentas de interação social, administrativas e empresariais. Pelo fato de, hoje em dia, as empresas utilizarem algum sistema informatizado, sempre terão a necessidade de um profissional para administrá-lo. Com isso, o mercado de trabalho para esta área se mantém aquecido, com uma demanda muito alta por profissionais qualificados. Na maioria das vezes, garante ótimas remunerações. Dependendo da formação e do tempo de experiência, este profissional poderá assumir diferentes cargos em empresas dos mais diversos setores. Veja alguns exemplos: Administrador de Banco de Dados (DBA), Consultor de Banco de Dados, Analista de Dados, Analista de Suporte, Desenvolvedor de Projetos de Banco de Dados e Gerente de Sistemas de Bancos de Dados."
        }
    return render(request, "descricaocursos.html", contexto)
    
def desc_redes(request):
    contexto={
        "titulo":"Descrição de Curso Redes",
        "descricao":"O curso prepara o aluno para elaborar, implantar e gerenciar projetos lógicos e físicos de redes de computadores locais e de longa distância. Redes Convergentes, Comunicações Óticas, Redes sem Fio e de Banda Larga estão entre as disciplinas da grade  curricular. Há também as ministradas nos laboratórios.", 
        "perfil": "Este profissional elabora, implanta, gerencia e mantém projetos lógicos e físicos de redes de computadores locais e de longa distância. Atua na conectividade entre sistemas heterogêneos, no diagnóstico e na solução de problemas relacionados à comunicação de dados, segurança de redes, avaliação de desempenho, configuração de serviços de rede e de sistema de comunicação de dados.",
        "mercado":"As oportunidades de trabalho estão distribuídas por áreas de TI de empresas públicas e privadas, empresas de telecomunicações e provedores de acesso. Mas o profissional pode atuar como autônomo.",
        "link_grade":[
            {"nome":"Verificar Curso de Redes" , "link":"/cursos/grade-redes/"}
        ]
    }
    return render(request, "descricaocursos.html", contexto)


def desc_bd_lp(request):
    contexto={
        "curso":"Disciplina: Linguagem de Programação",
        "descricao":"Descrição: Uma linguagem de programação é um método padronizado para comunicar instruções para um computador. É um conjunto de regras sintáticas e semânticas usadas para definir um programa de computador. Permite que um programador especifique precisamente sobre quais dados um computador vai atuar, como estes dados serão armazenados ou transmitidos e quais ações devem ser tomadas sob várias circunstâncias. Linguagens de programação podem ser usadas para expressar algoritmos com precisão.",
        }   
    return render(request, "descricaocursos.html", contexto)

def desc_bd_fbd(request):
    contexto={
        "curso":"Disciplina: Fundamento de Banco de Dados",
        "descricao":"Descrição: O treinamento irá abordar conteúdos relacionados a conceitos básicos e fundamentais para quem deseja trabalhar com Banco de Dados: persistência de dados, melhores práticas, modelos de BD.",
        }
    return render(request, "descricaocursos.html", contexto)
    
def desc_bd_dba(request):
    contexto={
        "curso":"Disciplina: Administração de Banco de Dados",
        "descricao":"Descrição: Administrador de banco de dados, comumente chamado de DBA (sigla em inglês de Database administrator), é o profissional responsável por gerenciar, instalar, configurar, atualizar e monitorar um banco de dados ou sistemas de bancos de dados.",
        }
    return render(request, "descricaocursos.html", contexto)
    



def grade_ads(request):
    contexto={
        "titulo":"Análise e Desenvolvimento de Sistemas",
        "disc_sem1":["Lógica de Programação", "Linguagem de Programação","Fundamentos de Banco de Dados","IoT", "Matemática Aplicada", "Comunicação e Expressão"],
        "disc_sem2":["Linguagem de Programação II","Linguagem SQL","Tecnologia Web","Engenharia de Software","Linguagem Brasileira de Sinais - LIBRAS","Linguagem SQL", "Ambiente de Desenvolvimento e Operação - DevOps","Gestão de Projetos"],
        "disc_sem3":["Desenvolvimento de Aplicações Distribuídas","Estrutura de Dados","Modelagem de Processos de Negócio","Interface Homem-Computadore","OPE1 - Oficina Projeto Empresa 1"],
        "disc_sem4":["Arquitetura e Projeto de Sistemas","Desenvolvimento para Dispositivos Móveis","Desenvolvimento para Internet das Coisas","Qualidade de Software","OPE2","Legislação Ética"]
        
    }
    return render(request, "base_grade.html", contexto)


def grade_bd(request):
    contexto={
        "titulo":"Análise e Desenvolvimento de Sistemas",
        "disc_sem1":["Lógica de Programação", "Linguagem de Programação","Fundamentos de Banco de Dados","IoT", "Matemática Aplicada", "Comunicação e Expressão"],
        "disc_sem2":["Análise Exploratória de Dados","Engenharia de Software","Desenvolvimento de Sistemas","Ambiente de Desenvolvimento","Linguagem Brasileira de Sinais - LIBRAS","Linguagem SQL"],
        "disc_sem3":["Business Intelligence","Developing Database","Estrutura de Dados","Data Analytics","OPE1 - Oficina Projeto Empresa 1"],
        "disc_sem4":["Administração de Banco de Dados","Qualidade de Governança de Dados","Segurança de Banco de Dados","Computação Cognitiva","OPE2","Legislação Ética"]
   
    }
    return render(request, "base_grade.html", contexto)


def grade_redes(request):
    contexto={
        "titulo":"Rede de Computadores",
        "disc_sem1":["Administração de Redes e Sistemas", "Arquitetura de Redes de Computadores","Cabeamento Estruturado","Comunicação e Expressão", "Fundamentos de Sistemas Operacionais", "Introdução à Internet das Coisas - IoT","Programação para Redes"],
        "disc_sem2":["Administração de Redes e Sistemas Operacionais Livres","Ambiente de Desenvolvimento e Operação - DevOps","Gestão de TI","Redes de Longa Distância","Linguagem Brasileira de Sinais - LIBRAS","Routing", "Segurança em Redes e Infraestrutura","Gestão de Projetos"],
        "disc_sem3":["Comunicação de Dados","Diagnóstico e Gerenciamento de Redes","Legislação e Ética","Oficina Projeto Empresa 2 - OPE2","Optativa (Sociedade e Sustentabilidade","Língua Brasileira de Sinais - LIBRAS)","Redes Convergentes","Segurança em Sistemas","Switching"],
        "disc_sem4":["Computação em Nuvem","Comunicações Móveis","Auditoria e Controle de TI","Oficina Projeto Empresa 3 - OPE3","Redes IPV6,Serviços de Redes de Computadores","Tópicos Especiais em Redes de Computadores"]
        
    }
    return render(request, "base_grade.html", contexto)


def login(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "login.html", contexto)

def index(request):   
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "index.html" , contexto)

def tabela_aluno(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "tabela_aluno.html", contexto)

