# -*- coding: utf-8 -*-
# @Author: Zhongshu Chen
# @Date:   2019-07-08

import torch
import torch.nn as nn
import torchvision

from torch.utils.data import DataLoader
from torch.autograd import Variable
from torchvision.datasets import MNIST
from torchvision import transforms

import datetime

class LeNet(nn.Module):

    def __init__(self):
        super(LeNet,self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1,6,5),
            nn.MaxPool2d(2,2),
            nn.Conv2d(6,16,5),
            nn.MaxPool2d(2,2)
        )

        self.fc = nn.Sequential(
            nn.Linear(256,120),
            nn.Linear(120,80),
            nn.Linear(80,10)
        )

    def forward(self, x):
        #print('x.size:',x.size())
        out = self.conv(x)
        #print('out.size:',out.size())
        out = out.view(out.size(0),-1)
        #print('out2.size:',out.size())
        out = self.fc(out)
        return out


class Trainer(object):

    def __init__(self,model,criterion):
        
        super(Trainer,self).__init__()
        self.model = model
        self.criterion = criterion

    def train(self,epoch,dataloader,optimizer):
        
        self.model.train()

        for i in range(epoch):
            sum = 0
            runloss = 0
            correct = 0

            for _,batch in enumerate(dataloader):

                input,target=batch
                sum += len(target)

                input = Variable(input)
                target = Variable(target)

                input = input.cuda()
                target = target.cuda()

                output = self.model(input)
                loss = self.criterion(output, target)
                optimizer.zero_grad()
 
                loss.backward()
                optimizer.step()
 
                runloss += loss.data

            epoch_loss=runloss/sum
            print("Epoch {:d} , epoch loss {:f} ".format(i + 1,epoch_loss))

if __name__ == '__main__':

    start = datetime.datetime.now()

    
    learning_rate = 1e-3
    batch_size = 64
    epoches = 10

    trans_img = transforms.ToTensor()

    trainset = MNIST('./data', train=True,download=True ,transform=trans_img)
    testset = MNIST('./data', train=False,download=True, transform=trans_img)

    print(trainset)

    trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)
    testloader = DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=4)

    lenet = LeNet()
    lenet = lenet.cuda()
     
    criterion = nn.CrossEntropyLoss(size_average=False)
    optimizer = torch.optim.SGD(lenet.parameters(), lr=learning_rate)

    trainer=Trainer(lenet,criterion)
    print('Start training.....')
    trainer.train(epoches,trainloader,optimizer)
    print('Finish training.')

    # test

    sum = 0
    runloss = 0
    correct = 0

    for _, batch in enumerate(testloader):

        input,target = batch
        sum += len(target)

        input = Variable(input)
        target = Variable(target)

        input = input.cuda()
        target = target.cuda()

        output = lenet(input)
        loss = criterion(output, target)

        runloss += loss.data
        _, predict = torch.max(output,1)

        correctnum = (predict == target).sum()
        correct += correctnum.data

    print('Now testing the network...')
    print('Start testing...')
    final_loss = runloss / sum
    ### Type Conversion
    final_correct = correct.float() / sum
    print("Test Result:  final loss {:f}   final correct {:f}".format(final_loss, final_correct))
    print('Finish testing.')

    end = datetime.datetime.now()
    print ('Running time:',end-start)