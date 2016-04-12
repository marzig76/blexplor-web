from __future__ import unicode_literals

from django.db import models


class Block(models.Model):
    block_height = models.IntegerField()
    magic_number = models.IntegerField()
    block_size = models.IntegerField()
    version = models.IntegerField()
    prev_hash = models.CharField(max_length=100)
    merkel_root = models.CharField(max_length=100)
    block_time = models.IntegerField()
    target = models.IntegerField()
    nonce = models.IntegerField()
    tx_count = models.IntegerField()

    def __str__(self):
        response = (
            "Block Height: " + str(self.block_height) + "<br />" +
            "Magic Number: " + str(self.magic_number) + "<br />" +
            "Block Size: " + str(self.block_size) + "<br />" +
            "Version: " + str(self.version) + "<br />" +
            "Prev Hash: " + str(self.prev_hash) + "<br />" +
            "Merkel Root: " + str(self.merkel_root) + "<br />" +
            "Block Time: " + str(self.block_time) + "<br />" +
            "Target: " + str(self.target) + "<br />" +
            "Nonce: " + str(self.nonce) + "<br />" +
            "Tx Count: " + str(self.tx_count)
        )
        return response


class Tx(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    version = models.IntegerField()
    tx_input_count = models.IntegerField()
    tx_output_count = models.IntegerField()
    lock_time = models.IntegerField()


class TxInput(models.Model):
    tx = models.ForeignKey(Tx, on_delete=models.CASCADE)
    prev_hash = models.CharField(max_length=100)
    index = models.IntegerField()
    script_bytes = models.IntegerField()
    sigscript = models.CharField(max_length=100)
    sequence = models.IntegerField()


class TxOutput(models.Model):
    tx = models.ForeignKey(Tx, on_delete=models.CASCADE)
    value = models.IntegerField()
    script_pk_bytes = models.IntegerField()
    script_pk = models.CharField(max_length=100)
