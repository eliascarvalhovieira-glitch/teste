# Raio X: The American Shoe Archive

Canal: https://www.youtube.com/@TheAmericanShoeArchive1
Dados coletados em **13/10/2026**: metadados públicos via yt-dlp + feed RSS do canal. A tabela completa está em [`dados_videos.csv`](dados_videos.csv), e o script em [`analise.py`](analise.py).

> **Limitação:** só dá para ver dados públicos (views, likes, duração, títulos, datas). Retenção, CTR, origem do tráfego e receita só aparecem no YouTube Studio do dono do canal. Nas seções abaixo, o que é inferência está marcado como tal.

---

## 1. Retrato do canal

| Métrica | Valor |
|---|---|
| Canal criado | 31/08/2026 (há ~6 semanas) |
| Inscritos | 1.280 |
| Vídeos | 38 (nenhum Short, nenhuma live) |
| Views totais | ~224 mil |
| Mediana de views por vídeo | ~800 |
| Duração média | ~37 min (de 29 a 43 min) |
| Frequência | **1 vídeo longo por dia**, sempre por volta das 16h UTC |
| Idioma | Inglês, público dos EUA |

**Proposta (da descrição do canal):** documentários sobre marcas, lojas e fábricas de calçados americanas esquecidas. Cada vídeo segue o arco *origem → auge → declínio → reinvenção ou desaparecimento*.

**Inferência sobre a produção:** são cerca de 23 horas de documentário publicadas em 42 dias, sem rosto na câmera. Isso é praticamente impossível sem um pipeline com IA (roteiro, narração e montagem com imagens de arquivo). Esse é o modelo de negócio, e é também um risco (ver seção 4).

---

## 2. O que está dando certo

### 2.1 Poucos hits carregam o canal
Os **4 vídeos mais vistos somam 77% de todas as views**:

| # | Vídeo | Views | Views/dia |
|---|---|---|---|
| 1 | What Happened to **Converse**? | 85.000 | ~3.400 |
| 2 | What Happened to **Sebago**, the Boat Shoe Brand That Became a Preppy Icon | 42.000 | ~2.470 |
| 3 | What Happened to **Reebok**? The Sneaker Giant That Overtook Nike | 24.000 | ~2.180 |
| 4 | What Happened to **Sperry**? The Boat Shoe That Became an American Preppy Uniform | 21.000 | ~750 |
| 5 | What Happened to **K-Swiss**? | 8.600 | ~610 |
| 6 | What Happened to **Eastbay**? (publicado há 2 dias) | 5.900 | **~2.950** ⬆ |
| 7 | What Happened to **Ewing Athletics**? | 5.900 | ~840 |
| 8 | What Happened to **DADA Supreme**? | 4.300 | ~1.075 |
| 9 | What Happened to **L.A. Gear**? | 3.300 | ~105 |
| 10 | What Happened to **PRO-Keds**? | 2.900 | ~150 |

Metade dos vídeos tem menos de 800 views. É o padrão de um canal novo: o algoritmo testa cada vídeo, e alguns "pegam" no tráfego de sugeridos/navegação.

### 2.2 Temas que mais performam

| Tema | Vídeos | Views totais | Mediana | Leitura |
|---|---|---|---|---|
| **Tênis ícone global** (Converse, Reebok, Crocs, Vans) | 4 | 111 mil | **12.750** | Marca que todo mundo conhece = melhor aposta |
| **Preppy / boat shoe / casual** (Sebago, Sperry, Bass, Rockport, Hush Puppies, Dexter) | 6 | 71 mil | **2.300** | Surpresa: o nicho preppy é a categoria mais consistente |
| **Tênis cult / nostalgia anos 80-90** (K-Swiss, Ewing, DADA, LA Gear, Pro-Keds…) | 11 | 28 mil | 1.000 | Basquete/hip-hop dos anos 90 está em alta nos vídeos recentes |
| **Varejo / redes de lojas** (Foot Locker, Eastbay, Footaction, Just For Feet, Kinney…) | 8 | 10 mil | 405 | Fraco. Exceção: **Eastbay**, que tem gancho nostálgico (o catálogo) |
| **Sapato social / fabricantes centenários** (Florsheim, J&M, Endicott Johnson, W.L. Douglas…) | 7 | 3,8 mil | 512 | O tema mais fraco do canal |
| **Botas de trabalho** (Red Wing, Wolverine) | 2 | 0,8 mil | 408 | Fraco |

**Conclusão:** quanto mais conhecida a marca e mais forte a memória afetiva (infância, adolescência, "eu tinha um desses"), mais views. Histórias corporativas de empresas que o público não lembra (P.W. Minor, W.L. Douglas, U.S. Shoe, Troop) ficam abaixo de 400 views.

### 2.3 A fórmula de embalagem (títulos, SEO e formato)
1. **Título padronizado:** `What Happened to [MARCA]? [gancho]`. "What happened to…" é uma busca real e muito usada, e o formato também funciona como curiosidade no feed.
2. **O gancho sempre tem um destes elementos:**
   - número ou dinheiro: *"$775M"*, *"1,400 stores"*, *"$2.4 Billion"*, *"9,000 dealers"*;
   - nome famoso: *Michael Jordan, Kareem, Magic, Pelé, Warren Buffett, U.S. Presidents*;
   - contraste ou tragédia: *"went bankrupt before Nike bought it"*, *"overtook Nike"*, *"nearly collapsed"*;
   - identidade cultural: *"preppy icon"*, *"American status symbol"*.
3. **Descrição otimizada:** abre com hashtags, traz um resumo em 4 ou 5 parágrafos com palavras-chave e um CTA de memória afetiva (*"share your favorite Eastbay memory in the comments"*). As tags seguem o padrão "What Happened to X", "History of X" e "Why X Closed".
4. **Vídeos longos (33–43 min):** muito tempo de exibição por clique. Isso favorece a monetização e as recomendações na TV, onde está o público mais velho e nostálgico.
5. **Volume diário:** muitas "tentativas" para o algoritmo achar os hits. Com 38 vídeos, o canal encontrou 4 hits.
6. **Inferência sobre o público:** a taxa de likes é baixa (0,4%–1% das views) e há poucos comentários. Isso sugere um público mais velho (35+), que assiste na TV e vem de recomendações, e não um público engajado de "sneakerheads".

### 2.4 Tendência recente
Nos últimos 7 dias a mediana por vídeo subiu para ~1.500 views, contra 400–800 nas semanas anteriores. Os vídeos de basquete/anos 90 (Eastbay, DADA, Ewing) estão ganhando tração rápido. É sinal de que o canal está ganhando autoridade no algoritmo.

### 2.5 Monetização (estimativa)
- Requisitos do YPP: 1.000 inscritos + 4.000 horas de exibição em 12 meses. Os inscritos já passaram. Com ~224 mil views em vídeos de ~37 min, mesmo uma retenção média de 5–7 minutos resulta em ~18–26 mil horas. **Provavelmente já é elegível.**
- Público dos EUA + nicho de negócios/história = um dos RPMs mais altos do YouTube.

---

## 3. Faz sentido replicar em outros países?

### 3.1 Ajuste importante: o canal é por idioma, não por país
O YouTube distribui por idioma. Então a pergunta certa é:
- **Português** → Brasil (+ Portugal)
- **Espanhol** → México + Espanha + toda a América Latina + hispânicos nos EUA, **num único canal**
- **Francês** → França + **Bélgica** (Valônia/Bruxelas) + Suíça + Quebec + África francófona

**A Bélgica sozinha não justifica um canal.** O mercado é pequeno e dividido entre francês e neerlandês. Ela entra como parte do canal em francês, com episódios como Brantano, Eram Bélgica e Torfs.

### 3.2 O que faz o modelo funcionar e o que precisa existir em cada mercado
O canal americano funciona por três motivos:
1. existem muitas marcas locais com memória afetiva;
2. existem marcas globais que todo mundo conhece (Converse, Reebok, Vans, Crocs);
3. a audiência paga um bom RPM.

| Critério | 🇧🇷 Brasil (PT) | 🇲🇽🇪🇸 Espanhol (MX+ES+LatAm) | 🇫🇷🇧🇪 Francês (FR+BE) |
|---|---|---|---|
| Tamanho da audiência no YouTube | Muito grande | **A maior** (soma de vários países) | Média |
| RPM / CPM | Baixo (CPM ~US$1,6) | Baixo no México/LatAm, bom na Espanha (CPM ~US$14) | Médio-alto |
| Estoque de marcas locais nostálgicas | **Excelente:** Kichute, Bamba, Conga, Rainha, Topper, Montreal, Ortopé, Samello, Azaleia, Olympikus, Melissa, Havaianas (virada), Mesbla, Netshoes/Centauro | Bom: **Calzado Canadá** (vendida à Coppel em 2002), Panam, Charly, Flexi, Price Shoes; Paredes (Elche), J'Hayber, Kelme, Munich, Victoria; Argentina (Topper, Flecha, Pampero) | Médio: Patrick, Kickers, Spring Court, Le Coq Sportif, Palladium, Aigle, Paraboot, Eram, André, Bata; Bélgica: Brantano |
| Interesse comprovado pelo tema | Sim: InfoMoney, Exame, Diário do Pará e Gazeta SP publicam "que fim levou o Kichute/Rainha" | Sim: Expansión e El CEO publicaram "¿Qué pasó con Zapaterías Canadá?" (2025) | Mais fraco, pouca nostalgia de marca popular |
| Marcas globais (Converse, Reebok, Vans, Crocs, Adidas×Puma, Nike) | Funcionam | Funcionam | Funcionam |
| **Veredito** | ✅ **Sim, é o mais promissor** | ✅ **Sim, num canal único em espanhol** | ⚠️ **Talvez, como 3ª prioridade** |

### 3.3 Recomendação

**1º: Brasil (português). Faz sentido.**
- O formato "Que fim levou…?" / "O que aconteceu com…?" já é consagrado na imprensa brasileira, e os anos 80/90 rendem muita nostalgia (Kichute, Conga, Bamba, Rainha, Topper).
- Combinar ~50% de marcas brasileiras com ~50% de marcas globais (Converse, Reebok, Vans, Crocs, Nike, Adidas×Puma, Mizuno, Asics), que foram os hits no canal original.
- Ponto de atenção: o RPM brasileiro é cerca de 5–8x menor que o americano. A receita precisa vir de **volume e de patrocínios/afiliados** (lojas de calçados, marketplaces, marcas que estão relançando, como Kichute/Bamba ou a Rainha da BR Sports).

**2º: Espanhol (um canal para México + Espanha + LatAm). Faz sentido.**
- Não fazer um canal só do México e outro só da Espanha. Um canal em espanhol neutro pega os dois mercados mais o resto da América Latina e o público hispânico dos EUA (que tem RPM alto).
- Pauta: marcas globais + Calzado Canadá, Panam, Charly, Flexi (MX) + Paredes, J'Hayber, Kelme, Munich (ES) + Topper/Flecha/Pampero (AR).

**3º: Francês (França + Bélgica). Só depois de validar os dois primeiros.**
- RPM melhor, mas audiência menor e menos estoque de nostalgia de marcas populares.
- Bom ângulo: Sebago, Palladium, Kickers, Le Coq Sportif, Spring Court, Bata/André/Eram, Brantano.

### 3.4 Teste barato antes de abrir canais
1. **Piloto de 10–15 vídeos** no canal em português (e/ou espanhol): metade sobre os temas globais que já provaram funcionar (Converse, Reebok, Vans, Crocs, Sebago/Sperry) e metade sobre 4–5 marcas locais fortes (Kichute, Rainha, Topper, Conga / Calzado Canadá, Panam, Paredes).
2. Ative as **faixas de áudio multilíngues (dublagem por IA do YouTube)**, liberadas para todos os criadores. Assim, os vídeos sobre marcas globais também alcançam o outro idioma sem custo extra. Use os números para decidir qual idioma merece um canal próprio.
3. Meça a mediana de views por vídeo nas primeiras 3–4 semanas. Se ficar acima de ~1.000, com algum hit acima de 20 mil, escale para 1 vídeo/dia.

### 3.5 Riscos
- **Política de "conteúdo inautêntico"** (YouTube, desde jul/2025): canais "produzidos em massa", com narrativas quase iguais ou slideshows com a mesma narração, podem perder a monetização. A defesa é ter pesquisa original, roteiro com fontes, edição de verdade, narração de qualidade (de preferência humana ou bem curada) e variedade visual.
- **Direitos de imagem:** logos, comerciais antigos e fotos de produtos. Use trechos curtos com comentário (uso transformativo) e evite comerciais inteiros.
- **Dependência de hits:** o canal original ainda tem mediana de ~800 views. O sucesso é real, mas está concentrado em 4 vídeos e o canal tem só 6 semanas. É cedo para chamar de modelo comprovado.
- **Precisão histórica:** a imprensa diverge sobre datas (por exemplo, falência da Brantano em 2017 ou 2020; Calzado Canadá foi *vendida*, não faliu). Erros factuais destroem credibilidade nos comentários.

---

## Fontes
- Dados do canal: páginas públicas do YouTube via yt-dlp e o feed RSS `youtube.com/feeds/videos.xml?channel_id=UC9eHJgqXkFDf1sgb51xTyTw` (13/10/2026)
- CPM por país (estimativas de mercado, não oficiais): [ytface.com](https://ytface.com/cpm-rates-by-country), [MilX](https://milx.app/en/trends/which-countries-have-the-best-youtube-cpm-rates-in-2025), [Travelpayouts](https://www.travelpayouts.com/blog/?p=3882)
- Política de conteúdo inautêntico: [Social Samosa](https://www.socialsamosa.com/news-2/youtube-clarifies-monetisation-policy-targeting-inauthentic-content-9493155), [Gulf News](https://gulfnews.com/technology/youtube-updates-monetisation-policies-ai-and-repetitive-content-ban-begins-july-15-1.500192660)
- Áudio multilíngue / dublagem automática: [TechCrunch](https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/), [Metricool](https://metricool.com/youtube-multi-language-audio/)
- Brasil: [InfoMoney – Kichute](https://www.infomoney.com.br/business/kichute-que-fim-levou-o-calcado-que-marcou-a-infancia-dos-anos-1970/), [Exame – Kichute](https://exame.com/negocios/kichute-o-que-aconteceu-com-a-marca-de-tenis-que-bombava-nos-anos-80), [Diário do Pará – Rainha](https://diariodopara.com.br/cotidiano/o-que-aconteceu-com-a-rainha-marca-de-tenis-marcou-geracoes/), [Gazeta SP](https://www.gazetasp.com.br/gazeta-mais/conga-kichute-rainha-tenis-brasileiros-foram-sucesso-nos-anos-1980/)
- México: [Expansión – Zapaterías Canadá](https://expansion.mx/empresas/2025/08/30/que-paso-con-las-zapaterias-canada-coppel), [Milenio](https://www.milenio.com/negocios/calzado-canada-en-guadalajara-cual-es-su-historia), [El CEO](https://elceo.com/negocios/que-paso-con-las-zapaterias-canada-este-fue-su-destino/)
- Espanha: [The Olive Press – José Paredes](https://theolivepress.es/spain-news/2021/06/19/death-of-jose-paredes-who-pioneered-big-scale-shoe-manufacturing-in-elche-on-spains-costa-blanca)
- Bélgica/França: [Brussels Times – Brantano](https://brusselstimes.com/128489/brantano-liquidation-whats-going-on), [Paperjam](https://paperjam.lu/article/faillite-brantano-est-enterine), [RTBF – Eram](https://www.rtbf.be/article/la-chaine-de-magasins-de-chaussures-eram-cesse-ses-activites-en-belgique-9517913)
