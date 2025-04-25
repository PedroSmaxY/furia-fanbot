from fastapi import APIRouter, HTTPException, Query
from bs4 import BeautifulSoup
from core.scraper import get_html
from typing import Dict, Any

router = APIRouter(prefix="/api/debug", tags=["debug"])


@router.get("/debug_html", summary="Debug de qualquer URL do HLTV")
async def debug_html(
        url: str = Query(
            ...,
            description="URL completa para analisar (ex: https://www.hltv.org/team/8297/furia)",
        )
) -> Dict[str, Any]:
    """
    Retorna o HTML bruto de qualquer URL para análise e debug.
    Permite examinar a estrutura antes de implementar parsers específicos.

    - url: URL completa da página a ser analisada
    """
    try:
        html = get_html(url)

        if not html:
            raise HTTPException(
                status_code=503, detail="Não foi possível obter dados da URL"
            )

        soup = BeautifulSoup(html, "html.parser")

        page_info = {
            "url": url,
            "title": soup.title.text if soup.title else "Sem título",
            "html_length": len(html),
            "total_elements": len(soup.find_all()),
        }

        element_counts = {}
        for tag in soup.find_all():
            tag_name = tag.name
            if tag_name in element_counts:
                element_counts[tag_name] += 1
            else:
                element_counts[tag_name] = 1

        page_info["element_counts"] = element_counts

        tables = soup.find_all("table")
        table_structures = []

        for i, table in enumerate(tables):
            table_classes = table.get("class", [])
            table_id = table.get("id", "")

            headers = [th.text.strip() for th in table.find_all("th")]

            sample_row = []
            first_row = table.find("tr")
            if first_row and first_row.find_all("td"):
                sample_row = [td.text.strip() for td in first_row.find_all("td")]

            table_structures.append(
                {
                    "index": i,
                    "id": table_id,
                    "classes": table_classes,
                    "headers": headers,
                    "row_count": len(table.find_all("tr")) - (1 if headers else 0),
                    "sample_row": sample_row,
                }
            )

        page_info["tables"] = table_structures

        main_texts = []
        for heading in soup.find_all(["h1", "h2", "h3"]):
            main_texts.append(heading.text.strip())

        page_info["main_headings"] = main_texts[:10]
        html_preview = html[:5000]
        page_info["html_preview"] = html_preview

        css_classes = {}
        for tag in soup.find_all(True, class_=True):
            for css_class in tag.get("class", []):
                if css_class in css_classes:
                    css_classes[css_class] += 1
                else:
                    css_classes[css_class] = 1

        sorted_classes = sorted(css_classes.items(), key=lambda x: x[1], reverse=True)
        page_info["common_css_classes"] = dict(sorted_classes[:20])

        return {"status": "success", "data": page_info}
    except Exception as e:
        print(f"Erro ao analisar HTML: {str(e)}")
        return {"status": "error", "message": str(e)}
