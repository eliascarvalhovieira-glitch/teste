# Contexto: canal Old Earl's Workbench

Cole isto no início de uma nova conversa. Você vai me ajudar a crescer este canal do YouTube usando o método "Brecha Viral".

## 1. O canal
- Nome: Old Earl's Workbench (@OldEarlsWorkbench). É um canal faceless, em inglês, para o público dos EUA.
- Persona: "Old Earl", um senhor experiente de oficina. O tom é nostálgico e desconfiado das grandes marcas ("as ferramentas antigas eram melhores").
- Nicho: ferramentas manuais e elétricas, oficina e marcas de ferramenta.
- Formato: vídeos longos, de 19 a 30 minutos.
- Público: homens mais velhos, americanos, que fazem DIY ou já foram profissionais.

## 2. Desempenho (em 23/11/2026: 7 inscritos, 7 vídeos)
| Vídeo | Views | Observação |
|---|---|---|
| ShopSmith Is BACK Why This Old School Shop Legend's Comeback Is Bad News for Big Brands | 1,2 mil | **O melhor, 5,1x acima da média do canal** |
| 12 Power Tool Mistakes That Are ILLEGAL in America (Most DIYers Don't Know) (2026) | 440 | 1,8x, formato de "segredo útil" |
| Harbor Freight Is Selling Snap-On Lookalikes for a Fraction of the Price. Then Comes the Catch. | 255 | produto concreto com pegadinha |
| 9 Tool Brands That Aren't What They Used to Be (Your Old Ones Were Better) | 194 | fraco |
| Stanley Black & Decker Just Dropped a Bombshell: Factories Closing and Prices Going Up | 127 | fraco (notícia de empresa) |
| The Feds Sued DeWalt's Owner Over 1.3 Million Saws (They've Been Caught 5 Times Before) | 65 | travou |
| 3 Companies Control Almost Every Lock On Your Front Door (The Brand Name Lie) | 14 | fracassou (saiu do tema de ferramentas) |

### O que aprendemos
- **Funciona:** a história de uma lenda antiga (ShopSmith) e o segredo útil que o DIYer não conhece ("Most DIYers Don't Know"). Produto concreto com pegadinha também vai razoavelmente.
- **Não funciona:** notícia de empresa, vídeos sobre "quem é dono de quem" e marcas que pioraram.
- **Não sair do tema de ferramentas.** O teste com fechaduras provou que o canal ainda é novo demais para mudar de assunto.
- O ShopSmith é o assunto vencedor. Vale explorar mais vídeos sobre ele.

## 3. O método Brecha Viral (resumo)
**Formato validado + assunto vizinho = brecha.** Não é copiar o vídeo. É reaproveitar a mecânica do título num assunto que ainda não tem dono.

Os 4 passos:
1. **Garimpar** um vídeo que estourou recentemente.
2. **Dissecar** o título.
3. **Encontrar** a brecha.
4. **Ocupar** o espaço antes dos outros.

As 5 peças típicas de um título:
- número alto;
- objeto concreto;
- segredo;
- autoridade emprestada;
- medo útil.

Os 5 tipos de brecha:
- **ângulo contrário:** inverter a premissa;
- **público excluído:** atender quem ficou de fora;
- **recorte de situação:** um momento específico;
- **prova e teste:** testar o que o outro só afirmou;
- **formato em outro nicho:** levar a estrutura para outro tema.

## 4. Regras de trabalho
1. **Antes de sugerir uma brecha, pesquise no próprio YouTube** se alguém já fez. Mostre só as que ainda não foram feitas e diga o que encontrou (título, canal, views).
2. **Checar os fatos** de qualquer afirmação do título ou do roteiro. Não inventar números nem participações de mercado. Se algo vier da memória e não de uma fonte, avisar "confirmar antes de gravar".
3. **Nada de título enganoso.** Por exemplo, "Just Sued" para um processo de 11 meses atrás. Esse público aponta o erro nos comentários.
4. **Avaliar todo título contra os dados do canal** (tabela acima), não só contra o método.
5. Evitar o "99%" exagerado. Para essa persona funciona melhor "Most DIYers / Most Owners Don't Know".
6. Datas do título (Black Friday etc.) fazem o vídeo expirar. Prefira colocá-las no roteiro e na descrição, ou trocar o título depois.

## 5. O que já foi pesquisado
- **Saturado no YouTube:**
  - "2 Companies Control 65% Of Your Tools (The Brand Name Lie)", com versões para Canadá, Austrália, Reino Unido, em espanhol e em português.
  - O mesmo formato em cortador de grama, tool trucks, Harbor Freight, tinta, HVAC, barcos, trailers (RV), trator, motosserra, gerador, churrasqueira, munição, pesca, carpete e bateria de carro.
  - Armadilha da bateria, história da DeWalt pintada de amarelo, fábrica da Craftsman no Texas, Chervon (dona de EGO, FLEX e Skil).
  - Segredos de trena e de parafusadeira de impacto, segredos da Harbor Freight.
- **Fatos confirmados:**
  - O DOJ processou a Stanley Black & Decker em 22/12/2025 por atrasar avisos de defeito em cerca de 1,3 milhão de serras de esquadria DeWalt (571 relatos, 9 cortes) e em cerca de 145 mil barras de demolição DeWalt.
  - A empresa já tinha fechado acordos sobre acusações parecidas em 1986, 1991, 1999, 2011 e 2015. Ela nega as acusações.

## 6. Próximos vídeos sugeridos (ainda não feitos)
1. **"This SECRET ShopSmith Rule Is NOT Known to Most Owners (Ignore It and It Breaks)"**
   - O segredo: o controle de velocidade do Mark V só deve ser girado com o motor ligado.
   - Confirmar no manual antes de gravar.
2. **"This SECRET ShopSmith Mode Is NOT Known to Most Owners (USE IT NOW!)"**
   - O Mark V montado como furadeira horizontal.
3. **"This SECRET Craftsman Rule Is NOT Known to Most Owners (Your Old Sears Tools Still Count)"**
   - O segredo: a garantia vitalícia das ferramentas manuais Craftsman antigas.
   - Existe procura (um vídeo de troca na Lowe's tem 822 mil views).
   - Confirmar a política atual, porque há relatos de a Lowe's recusar trocas.

## 7. Como pesquisar no YouTube (se você tiver acesso a terminal)
A busca web comum não indexa bem o YouTube. O que funcionou foi baixar `https://www.youtube.com/results?hl=en&gl=US&search_query=<termos>` com curl e ler o JSON `ytInitialData`, procurando os objetos `videoRenderer` (título, canal, views e data).
