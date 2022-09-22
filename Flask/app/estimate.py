from transformers import BertModel
from torch import nn
from transformers import BertTokenizer
import torch
import numpy as np
import pytorch_lightning as pl


class BertForSequenceClassifier_pl(pl.LightningModule):
    def __init__(self, model_name, lr, num_class):
        super().__init__()
        self.save_hyperparameters()
        self.bert = BertModel.from_pretrained(model_name)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_class)
        self.criterion = nn.CrossEntropyLoss()
        for param in self.bert.parameters():
            param.requires_grad = False
        for param in self.bert.encoder.layer[-1].parameters():
            param.requires_grad = True


def geo_code_estimater(name, region="全国"):
    if region == "東京":
        arg2mesh = [
            523871,
            523872,
            523873,
            523874,
            523875,
            523876,
            523877,
            523970,
            523971,
            523972,
            523973,
            523974,
            523975,
            523976,
            523977,
            533800,
            533802,
            533803,
            533804,
            533805,
            533806,
            533807,
            533811,
            533812,
            533813,
            533814,
            533815,
            533816,
            533817,
            533820,
            533821,
            533822,
            533823,
            533824,
            533825,
            533826,
            533827,
            533830,
            533831,
            533832,
            533833,
            533834,
            533835,
            533836,
            533837,
            533840,
            533841,
            533842,
            533843,
            533844,
            533845,
            533846,
            533847,
            533850,
            533851,
            533852,
            533853,
            533854,
            533855,
            533856,
            533857,
            533860,
            533861,
            533862,
            533863,
            533864,
            533865,
            533866,
            533867,
            533870,
            533871,
            533872,
            533873,
            533874,
            533875,
            533876,
            533877,
            533900,
            533901,
            533902,
            533903,
            533904,
            533905,
            533906,
            533907,
            533910,
            533911,
            533912,
            533913,
            533914,
            533915,
            533916,
            533917,
            533920,
            533921,
            533922,
            533923,
            533924,
            533925,
            533926,
            533927,
            533930,
            533931,
            533932,
            533933,
            533934,
            533935,
            533936,
            533937,
            533940,
            533941,
            533942,
            533943,
            533944,
            533945,
            533946,
            533947,
            533950,
            533951,
            533952,
            533953,
            533954,
            533955,
            533956,
            533957,
            533960,
            533961,
            533962,
            533963,
            533964,
            533965,
            533966,
            533967,
            533970,
            533971,
            533972,
            533973,
            533974,
            533975,
            533976,
            533977,
            543800,
            543801,
            543802,
            543803,
            543804,
            543805,
            543806,
            543807,
            543810,
            543811,
            543812,
            543813,
            543814,
            543815,
            543816,
            543817,
            543820,
            543821,
            543822,
            543823,
            543824,
            543825,
            543826,
            543827,
            543837,
            543900,
            543901,
            543902,
            543903,
            543904,
            543905,
            543906,
            543907,
            543910,
            543911,
            543912,
            543913,
            543914,
            543915,
            543916,
            543917,
            543920,
            543921,
            543922,
            543923,
            543924,
            543925,
            543926,
            543927,
            544010,
            544020,
        ]
        code_estimate_model_path = (
            "/home/is/shuntaro-o/dev/SharedTask_FlaskApp/Flask/app/models/tokyo.ckpt"
        )
    elif region == "京都":
        arg2mesh = [
            523477,
            523515,
            523516,
            523517,
            523524,
            523525,
            523526,
            523527,
            523533,
            523534,
            523535,
            523536,
            523537,
            523542,
            523543,
            523544,
            523545,
            523546,
            523551,
            523552,
            523553,
            523554,
            523555,
            523556,
            523560,
            523561,
            523562,
            523563,
            523564,
            523565,
            523566,
            523570,
            523571,
            523572,
            523573,
            523574,
            523575,
            523576,
            523610,
            533407,
            533426,
            533427,
            533436,
            533437,
            533447,
            533500,
            533501,
            533502,
            533503,
            533504,
            533505,
            533506,
            533510,
            533511,
            533512,
            533513,
            533514,
            533520,
            533521,
            533522,
            533523,
            533530,
            533531,
            533532,
            533533,
            533540,
            533541,
            533542,
            533543,
        ]
        code_estimate_model_path = (
            "/home/is/shuntaro-o/dev/SharedTask_FlaskApp/Flask/app/models/Kyoto.ckpt"
        )
    elif region == "奈良":
        arg2mesh = [
            503575,
            503576,
            503577,
            503670,
            503671,
            513505,
            513506,
            513507,
            513515,
            513516,
            513517,
            513525,
            513526,
            513527,
            513535,
            513536,
            513537,
            513545,
            513546,
            513547,
            513555,
            513556,
            513557,
            513565,
            513566,
            513567,
            513575,
            513576,
            513577,
            513600,
            513601,
            513610,
            513611,
            513620,
            513621,
            513630,
            513631,
            513640,
            513641,
            513650,
            513651,
            513660,
            513661,
            513670,
            513671,
            523505,
            523506,
            523507,
            523600,
            523601,
        ]
        code_estimate_model_path = (
            "/home/is/shuntaro-o/dev/SharedTask_FlaskApp/Flask/app/models/Nara.ckpt"
        )
    elif region == "全国" or region == None:
        arg2mesh = [
            3927,
            3928,
            3933,
            3942,
            3945,
            4027,
            4028,
            4033,
            4037,
            4040,
            4042,
            4043,
            4128,
            4129,
            4130,
            4133,
            4134,
            4135,
            4140,
            4142,
            4143,
            4228,
            4229,
            4231,
            4233,
            4236,
            4243,
            4330,
            4331,
            4332,
            4340,
            4428,
            4432,
            4442,
            4530,
            4531,
            4532,
            4539,
            4540,
            4541,
            4542,
            4628,
            4630,
            4631,
            4632,
            4639,
            4640,
            4641,
            4729,
            4730,
            4731,
            4732,
            4739,
            4828,
            4829,
            4830,
            4831,
            4832,
            4837,
            4838,
            4841,
            4842,
            4844,
            4845,
            4928,
            4929,
            4930,
            4931,
            4932,
            4933,
            4934,
            4937,
            4938,
            4939,
            4940,
            5029,
            5030,
            5031,
            5032,
            5033,
            5034,
            5035,
            5036,
            5037,
            5039,
            5040,
            5041,
            5042,
            5128,
            5129,
            5130,
            5131,
            5132,
            5133,
            5134,
            5135,
            5136,
            5137,
            5138,
            5139,
            5140,
            5141,
            5142,
            5144,
            5227,
            5228,
            5229,
            5231,
            5232,
            5233,
            5234,
            5235,
            5236,
            5237,
            5238,
            5239,
            5240,
            5241,
            5242,
            5243,
            5244,
            5332,
            5333,
            5334,
            5335,
            5336,
            5337,
            5338,
            5339,
            5340,
            5341,
            5342,
            5434,
            5436,
            5437,
            5438,
            5439,
            5440,
            5441,
            5442,
            5444,
            5445,
            5536,
            5537,
            5538,
            5539,
            5540,
            5541,
            5542,
            5543,
            5544,
            5545,
            5630,
            5636,
            5637,
            5638,
            5639,
            5640,
            5641,
            5642,
            5643,
            5644,
            5645,
            5736,
            5738,
            5739,
            5740,
            5741,
            5742,
            5743,
            5744,
            5745,
            5839,
            5840,
            5841,
            5842,
            5843,
            5844,
            5935,
            5937,
            5939,
            5940,
            5941,
            5942,
            5943,
            5944,
            5945,
            6038,
            6039,
            6040,
            6041,
            6042,
            6043,
            6044,
            6139,
            6140,
            6141,
            6142,
            6143,
            6239,
            6240,
            6241,
            6242,
            6243,
            6244,
            6339,
            6340,
            6341,
            6342,
            6343,
            6344,
            6345,
            6432,
            6437,
            6439,
            6440,
            6441,
            6442,
            6443,
            6444,
            6445,
            6446,
            6537,
            6540,
            6541,
            6542,
            6543,
            6544,
            6545,
            6636,
            6640,
            6641,
            6642,
            6643,
            6644,
            6645,
            6741,
            6742,
            6743,
            6745,
            6830,
            6831,
            6840,
            6841,
            6843,
        ]
        code_estimate_model_path = "/home/is/shuntaro-o/dev/SharedTask_FlaskApp/Flask/app/models/japan_model.ckpt"
    tokenizer = BertTokenizer.from_pretrained(
        "cl-tohoku/bert-base-japanese-whole-word-masking"
    )
    model = BertForSequenceClassifier_pl.load_from_checkpoint(code_estimate_model_path)
    bert = model.bert.cuda()
    classifier = model.classifier.cuda()
    text = name
    encoding = tokenizer(
        text,
        max_length=107,  # 文章の長さを固定（Padding/Trancatinating）
        pad_to_max_length=True,  # PADDINGで埋める
        truncation=True,
        padding="longest",
        return_tensors="pt",
    )
    encoding = {k: v.cuda() for k, v in encoding.items()}
    with torch.no_grad():
        output = bert(**encoding)
        ans = classifier(output.pooler_output)
        ans = ans.to("cpu").detach().numpy().copy()
        ans = np.argmax(ans)
        geo_code = arg2mesh[ans]
    return geo_code
