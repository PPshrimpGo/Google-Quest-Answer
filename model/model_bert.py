from transformers import *
import torch
import torch.nn as nn
import torch.nn.functional as F

############################################ Define Net Class
class QuestNet(nn.Module):
    def __init__(self, model_type="bert-base-uncased", n_classes=30):
        super(QuestNet, self).__init__()
        self.model_name = 'QuestModel'
        self.bert_model = BertModel.from_pretrained(model_type)    
        self.fc = nn.Linear(768, n_classes)


    def forward(self, ids, seg_ids):
        attention_mask = (ids > 0)
        sequence_out, pool_out = self.bert_model(input_ids=ids, token_type_ids=seg_ids, attention_mask=attention_mask)
        # sequence_out, N * 512 * 768
        # pooled_out = N * 768

        # use pooled_out
        # out = F.dropout(pooled_out, p=0.2, training=self.training)

        # use sequence_out + global_average_pooling
        out = torch.squeeze(torch.mean(sequence_out, dim=1))
        # out N * 768
        out = F.dropout(out, p=0.2, training=self.training)
        logit = self.fc(out)

        return logit

############################################ Define test Net function
def test_Net():
    print("------------------------testing Net----------------------")

    x = torch.tensor([[1, 2, 3, 4, 5, 0, 0], [1, 2, 3, 4, 5, 0, 0]])
    seg_ids = torch.tensor([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    model = QuestNet()

    y = model(x, seg_ids)
    print(y)

    print("------------------------testing Net finished----------------------")

    return


if __name__ == "__main__":
    test_Net()