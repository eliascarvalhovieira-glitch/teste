# Contexto: canal de tratores

Cole isto no início de uma nova conversa. Você vai me ajudar a crescer um canal do YouTube no nicho de **tratores**, usando o método "Brecha Viral".

## 1. O canal (preencher)
- Nome / @:
- Idioma e país do público:
- Persona / narrador:
- Formato (duração média, faceless ou não):
- Público:
- Vídeos já postados e desempenho: (colar a lista com views, VPH e idade de cada vídeo)

## 2. O método Brecha Viral
**Formato validado + assunto vizinho = brecha.** Não é copiar o vídeo. É reaproveitar a mecânica de um título que já estourou num assunto que ainda não tem dono. O vídeo original ficou com a audiência por ter chegado antes, não por ser melhor. Disputar o mesmo espaço depois é perda de tempo. O valor está no espaço vizinho ainda vazio.

Os 4 passos:
1. **Garimpar** um vídeo que já estourou. Quanto mais recente, melhor o sinal.
2. **Dissecar** o formato: quais são as peças do título, que público ele atinge, por que segura a pessoa.
3. **Encontrar** a brecha: que assunto vizinho cabe nesse formato e ainda não tem dono.
4. **Ocupar** o espaço: mesmas peças, assunto novo, chegando primeiro.

As 5 peças típicas de um título:
- **número alto:** promete volume e justifica um vídeo longo;
- **objeto concreto:** gera uma imagem mental na hora;
- **segredo:** informação que o outro lado não tem;
- **autoridade emprestada:** credibilidade sem precisar de rosto;
- **medo útil:** faz clicar, e a lista faz ficar.

Os 5 tipos de brecha:
- **ângulo contrário:** inverter a premissa;
- **público excluído:** atender quem ficou de fora;
- **recorte de situação:** um momento específico;
- **prova e teste:** testar na prática o que o outro só afirmou;
- **formato em outro nicho:** levar a estrutura inteira para outro tema.

## 3. Regras de trabalho
1. **Antes de sugerir uma brecha, pesquise no próprio YouTube** se alguém já fez. Mostre só as que ainda não foram feitas, com a evidência (título, canal, views e idade do que já existe).
2. **Checar os fatos** de qualquer afirmação do título ou do roteiro. Não inventar números nem participações de mercado. Se algo vier da memória e não de uma fonte, avisar "confirmar antes de gravar".
3. **Nada de título enganoso** (por exemplo, "Just" para uma notícia antiga). O público aponta nos comentários e o canal perde credibilidade.
4. **Avaliar todo título contra os dados do próprio canal**, não só contra o método: o que já funcionou e o que não funcionou.
5. **Canal novo não deve sair do tema.** Até o YouTube entender o público, mantenha cada vídeo dentro do nicho de tratores.
6. Datas no título (Black Friday, ano etc.) fazem o vídeo expirar. Prefira colocá-las no roteiro e na descrição, ou trocar o título depois.
7. Espaço vazio não prova que há demanda. Confira se o público procura o assunto, por exemplo com vídeos vizinhos que tenham muitas views.

## 4. Pesquisa prévia sobre o nicho (de 21/11/2026; atualize antes de usar)
Já existem estes vídeos no formato "marcas que são a mesma empresa":
- "The Tractor Brands That Are Secretly the Same Machine (You're Paying Double for a Badge)" (Iron and Acreage), com 391 mil views, e uma Parte 2.
- "The Tractor Brands That Are Secretly Owned by the Same Company (The Brand Name Lie)" (FieldWorksCo).
- "ONLY THESE Compact Tractor Brands Make Their Own Tractors!!" (Tractor Time with Tim), com 408 mil views.
- Variações como "Only Tractor Brands Still Built in America", "Tractor Brands Going Out of Business" e "4 Tractor Brands Better Than John Deere".

Ou seja, o ângulo de quem é dono de quem já está ocupado nesse nicho. Procure outras brechas.

## 5. Como pesquisar no YouTube (se você tiver acesso a terminal)
A busca web comum não indexa bem o YouTube. O que funcionou foi baixar `https://www.youtube.com/results?hl=en&gl=US&search_query=<termos>` com curl e ler o JSON `ytInitialData`, procurando os objetos `videoRenderer` (título, canal, views e data).
