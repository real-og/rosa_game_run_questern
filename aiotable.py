import gspread_asyncio
from google.oauth2.service_account import Credentials
from loader import SHEET_LINK
import datetime

link = SHEET_LINK
def get_creds():
    creds = Credentials.from_service_account_file("key.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
async def get_sheet(agcm=agcm):
    agc = await agcm.authorize()
    ss = await agc.open_by_url(link)
    zero_ws = await ss.get_worksheet(0)
    return zero_ws


async def append_user(id: str, username: str, phone_num):
    sheet = await get_sheet()
    await sheet.append_row([str(id), str(username), str(phone_num)])

             
        
async def update_cell(id, cell_num, value):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, cell_num, str(value))