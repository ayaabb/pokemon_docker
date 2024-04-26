from fastapi import APIRouter, HTTPException,Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from utils.pokemon_utils import scrape_data, get_attributes

router = APIRouter()
pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
templates = Jinja2Templates(directory="templates")


@router.get('/pokemons/{pokemon_name}', response_class=HTMLResponse)
async def get_pokemon_data(request: Request, pokemon_name: str):
    response = scrape_data(pokemon_url, pokemon_name.lower())
    if response.status_code == 200:
        attributes = get_attributes(response.json(),pokemon_name)
        return templates.TemplateResponse("pokemon_data.html", {"request": request, "attributes": attributes})
    else:
        raise HTTPException(status_code=404, detail="Pokemon not found")
