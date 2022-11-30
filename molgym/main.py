# main.py

from typing import Optional
from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

import os

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    cmd: str

app = FastAPI()

@app.post("/train")
async def create_item_train(item: Item):
    # python3 scripts/run.py --name=SF6 --symbols=X,F,S --formulas=SF6 --min_mean_distance=1.10 --max_mean_distance=2.10  --bag_scale=5 --beta=-10 --model=covariant  --canvas_size=7 --num_envs=10 --num_steps=15000 --num_steps_per_iter=140  --mini_batch_size=140 --save_rollouts=eval --device=cpu --seed=1
    cmd = item.cmd
    os.system(cmd + " > out2.txt &")
    return {"result": "Training Started"}

@app.post("/train-info")
async def create_item_train_info():
    # python3 scripts/run.py --name=SF6 --symbols=X,F,S --formulas=SF6 --min_mean_distance=1.10 --max_mean_distance=2.10  --bag_scale=5 --beta=-10 --model=covariant  --canvas_size=7 --num_envs=10 --num_steps=15000 --num_steps_per_iter=140  --mini_batch_size=140 --save_rollouts=eval --device=cpu --seed=1
    # cmd = item.cmd
    # os.system(cmd + " > out2.txt")
    f = open('out2.txt', "r")
    text = f.readlines()
    fulltext = ""
    for i in text[-20:]:
        fulltext = fulltext + i
    f.close()
    return {"result": fulltext}

@app.post("/eval-plot")
async def create_item_eval_plot( item: Item):
    # python3 scripts/plot.py --dir=results
    cmd = item.cmd

    os.system(cmd + " > out.txt")

    f = open('out.txt', "r")
    text = f.readlines()
    fulltext = ""
    for i in text:
        fulltext = fulltext + i
    f.close()
    return {"result": fulltext}


@app.post("/eval-structures")
async def create_item_eval_structures(item: Item):
    # python3 scripts/structures.py --dir=data --symbols=X,F,S
    cmd = item.cmd

    os.system(cmd + " > out3.txt")

    f = open('out3.txt', "r")
    text = f.readlines()
    fulltext = ""
    for i in text:
        fulltext = fulltext + i
    f.close()

    f = open('structures_eval.xyz', "r")
    text = f.readlines()
    fulltext2 = ""
    for i in text:
        fulltext2 = fulltext2 + i
    f.close()
    return {"result": fulltext, "stuctures_eval.xyz":fulltext2}

