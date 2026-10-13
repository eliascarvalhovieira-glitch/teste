"""Analise do canal The American Shoe Archive a partir dos metadados publicos (yt-dlp + RSS)."""
import csv, json, statistics as st, sys
from datetime import date, timedelta

# Categoria tematica de cada video (classificacao manual pelo titulo)
CAT = {
 "Foot Locker":"Varejo/redes de lojas","Eastbay":"Varejo/redes de lojas","Footaction":"Varejo/redes de lojas",
 "Just For Feet":"Varejo/redes de lojas","Kinney":"Varejo/redes de lojas","Thom McAn":"Varejo/redes de lojas",
 "U.S. Shoe":"Varejo/redes de lojas","Nine West":"Varejo/redes de lojas",
 "Converse":"Tenis icone (gigante)","Reebok":"Tenis icone (gigante)","Vans":"Tenis icone (gigante)","Crocs":"Tenis icone (gigante)",
 "K-Swiss":"Tenis cult/nostalgia 80-90","Ewing":"Tenis cult/nostalgia 80-90","DADA":"Tenis cult/nostalgia 80-90",
 "L.A. Gear":"Tenis cult/nostalgia 80-90","PRO-Keds":"Tenis cult/nostalgia 80-90","PONY":"Tenis cult/nostalgia 80-90",
 "Troop":"Tenis cult/nostalgia 80-90","KangaROOS":"Tenis cult/nostalgia 80-90","Heelys":"Tenis cult/nostalgia 80-90",
 "P.F.Flyers":"Tenis cult/nostalgia 80-90","Earth Shoes":"Tenis cult/nostalgia 80-90",
 "Sebago":"Preppy/boat shoe/casual","Sperry":"Preppy/boat shoe/casual","G.H. Bass":"Preppy/boat shoe/casual",
 "Hush Puppies":"Preppy/boat shoe/casual","Rockport":"Preppy/boat shoe/casual","Dexter":"Preppy/boat shoe/casual",
 "Florsheim":"Sapato social/fabricantes historicos","Johnston & Murphy":"Sapato social/fabricantes historicos",
 "Cole Haan":"Sapato social/fabricantes historicos","Endicott Johnson":"Sapato social/fabricantes historicos",
 "W.L. Douglas":"Sapato social/fabricantes historicos","P.W. Minor":"Sapato social/fabricantes historicos",
 "Naturalizer":"Sapato social/fabricantes historicos",
 "Red Wing":"Botas de trabalho","Wolverine":"Botas de trabalho",
}
TODAY = date(2026, 10, 13)

def main(src, out):
    entries = json.load(open(src))["entries"]
    # Uploads diarios: o mais recente e 2026-10-12 (confirmado no RSS e por video);
    # datas inferidas pela ordem da playlist e conferidas com os 15 videos do RSS + 13 videos com metadados completos.
    rows = []
    for i, e in enumerate(entries):
        brand = min((k for k in CAT if k.lower() in e["title"].lower()), key=lambda k: e["title"].lower().index(k.lower()))
        up = date(2026, 10, 12) - timedelta(days=i + (1 if i >= 36 else 0))  # Dexter confirmado em 05/09
        days = (TODAY - up).days
        rows.append(dict(data_aprox=up.isoformat(), marca=brand, categoria=CAT[brand], views=e["view_count"],
                         duracao_min=round(e["duration"] / 60), views_por_dia=round(e["view_count"] / max(days, 1)),
                         titulo=e["title"], url=e["url"]))
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    total = sum(r["views"] for r in rows)
    print(f"videos={len(rows)} total_views={total} mediana={st.median(r['views'] for r in rows)} "
          f"duracao_media={st.mean(r['duracao_min'] for r in rows):.1f}min")
    top = sorted(rows, key=lambda r: -r["views"])
    print("top4 share", round(sum(r["views"] for r in top[:4]) / total * 100, 1), "%")
    for r in top[:10]: print(f"  {r['views']:>6} {r['data_aprox']} {r['marca']}")
    print("\nPor categoria: n | total | mediana | media | max")
    for c in sorted(set(CAT.values())):
        v = [r["views"] for r in rows if r["categoria"] == c]
        print(f"  {c:40} {len(v):>2} {sum(v):>7} {st.median(v):>7.0f} {st.mean(v):>7.0f} {max(v):>6}")
    print("\nPor duracao:")
    for lo, hi in [(0, 35), (35, 38), (38, 99)]:
        v = [r["views"] for r in rows if lo <= r["duracao_min"] < hi]
        print(f"  {lo}-{hi}min n={len(v)} mediana={st.median(v):.0f}")
    print("\nPor semana:")
    for k in range(0, 6):
        v = [r["views"] for r in rows if k * 7 <= (date(2026,10,12) - date.fromisoformat(r["data_aprox"])).days < (k+1) * 7]
        if v: print(f"  semana -{k}: n={len(v)} total={sum(v)} mediana={st.median(v):.0f}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
