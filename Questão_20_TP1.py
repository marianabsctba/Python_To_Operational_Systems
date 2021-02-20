import psutil

def size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        

def partition_info():
    p = psutil.disk_partitions() #já pressupõe o dispositivo corrente (o meu SO é windows, por exemplo, pelo que costumeiramente a questão 19 e 20 seriam parecidas em virtude do C:\\
    for partition in p:
        print(f"Nome do dispositivo: {partition.device}")
        print(f"Tipo de arquivo: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.device)
        except:
            print("Falhou. Tente novamente.")
            continue
        print(f"Armazenamento total: {size(partition_usage.total)}")
        print(f"Armazenamento disponível(livre): {size(partition_usage.free)}")
        
     
partition_info()
