def nossos_dias_nunca_voltarao():
    frase = list()
    paragrafos = """
    <p>E aí? Curtiu a Esco<u>l</u>a de <u>I</u>nverno deste ano? Para que esta Escola acontecesse, <u>f</u>oram muitos qu<u>e</u> trabalharam, seja na elaboração dos problemas, na conf<u>i</u>guração do Portal, na logí<u>s</u>tica do eve<u>n</u>t<u>o</u> ou na cap<u>ta</u>ção dos recursos. Nosso agradecimento es<u>p</u>ecial deste ano vai pa<u>r</u>a <u>o</u> Prof. Ricardo Oliveira, que não somente aceitou vir ministrar as oficinas como tam<u>b</u>ém participou ativamente na organização da Esco<u>l</u>a. T<u>em</u>os cer<u>t</u>eza que a experiência e a carreira dele n<u>o</u> ICPC como competidor e como <em>coach</em> motivaram e inspiraram todos nós.</p>
    <p>Esperamos que você tenha gostado desses últimos dias em Essos e em Westeros, que tenha aprendido <u>b</u>astant<u>e</u> e que tenha <u>s</u>e divertid<u>o</u>. Mas não é só em Essos e em Westeros que você deve se divertir. Aqui, em A<u>l</u>ém da Muralha, programar também é di<u>ve</u>rti<u>d</u>o. Continue estudando, continue treinando, e cada vez mais. O importante é o caminho que você vai trilhar daqui para frente. Nosso conselho é que você procure sempre aproveitar ao máximo cada momento, cada oficina, cada escola, cada treino, cada tempo de prática ou estudo em casa. Nossos dias nunca voltarão.</p>
    """
    palavras = paragrafos.split()
    for palavra in palavras:
        if '<u>' in palavra:
            for letter in palavra:
                pass


nossos_dias_nunca_voltarao()
