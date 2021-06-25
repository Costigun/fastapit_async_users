from fastapi import APIRouter, HTTPException

import requests

# set API's counter
from starlette import status

API_NUMS = 3


def send_request(url):
    return requests.get(url).json()


router = APIRouter(
    tags=['Second Task']
)


def shard_data(start_ranges, stop_ranges):
    result1 = [{'id': i, 'name': f'test{i}'} for i in range(*start_ranges)]
    result2 = [{'id': i, 'name': f'test{i}'} for i in range(*stop_ranges)]
    result1.extend(result2)
    return result1


@router.get('/remote/1')
async def first_view():
    raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail='WOw!')


@router.get('/remote/2')
async def first_view():
    data = shard_data((11, 20), (41, 50))
    return data


@router.get('/remote/3')
async def first_view():
    data = shard_data((21, 30), (51, 60))
    return data
