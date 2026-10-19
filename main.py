from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data_loader.bootstrap_loader import load as load_bootstrap_data
from utils.apis import get_teams

app = FastAPI()

# Point FastAPI to your templates folder
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    # Data to pass to the HTML template
    context_data = {
        'request': request,
        'title': 'Premier League',
        'items': get_teams()
    }
    return templates.TemplateResponse(request= request, name='home.html', context=context_data)

@app.post('/reload-teams')
def reload_teams():
    load_bootstrap_data(reload_teams_data=True)
    get_teams.cache_clear()
    return {'message': 'Teams data refreshed successfully.'}

def main():
    pass

if __name__ == '__main__':
    main()
