# Instruções do canal

## Quando o usuário mandar um roteiro de vídeo

Sempre que o usuário enviar um roteiro de vídeo, sem precisar pedir, monte a seção de produtos afiliados da Amazon para a descrição do vídeo:

1. **Analise o roteiro e defina o público**: quem assiste (idade, situação de vida, interesses) e o que essa pessoa estaria com vontade de comprar depois de ver o vídeo. **Os produtos não precisam estar no roteiro**; escolha o que esse público compraria de verdade.
   - Prefira produtos que a pessoa deseja e que funcionam como presente, não acessórios baratos e sem apelo.
   - Mantenha a coerência com a mensagem do vídeo. Exemplo: num vídeo sobre marcas que deixaram de fabricar no Reino Unido, não divulgue a versão fabricada fora.
   - **Pesquise na amazon.co.uk** (busca restrita ao domínio) e escolha **4 produtos**.
   - Confira em cada página se o produto está disponível e, quando importar para o tema, qual é o país de origem.
   - Descarte páginas indisponíveis. **Confira o estoque de cada link antes de entregar**: baixe a página (`curl` da URL `/dp/ASIN`) e procure no texto:
     - "Currently unavailable" = esgotado → descarte.
     - "This item cannot be dispatched to your selected delivery location" = **disponível** para o Reino Unido (o servidor está fora do país, por isso a mensagem).
     - "In stock" (quando a página aceita enviar para o local do servidor) = **disponível**.
     - "Page Not Found" = link morto → descarte.
   - A busca na web mostra cópias antigas das páginas: ela serve para achar produtos e confirmar a origem, não o estoque.
2. **Entregue em um único bloco de código pronto para copiar e colar**, em inglês (o público é britânico), neste formato:
   - Um título de seção com emoji.
   - Uma frase curta de abertura que ligue os produtos ao vídeo.
   - Para cada produto: emoji + nome, uma copy de 2 a 4 frases que faça referência a fatos do roteiro, e `👉 <link da Amazon>`.
   - No final, o aviso obrigatório: "As an Amazon Associate I earn from qualifying purchases. The links above are affiliate links, so I may earn a small commission at no extra cost to you."
3. Use links limpos (`https://www.amazon.co.uk/.../dp/ASIN`). O usuário troca pelos links de afiliado dele.
4. Fora do bloco de código, responda em português e só com o essencial: produtos descartados e por quê, e o que o usuário deve conferir antes de publicar.
