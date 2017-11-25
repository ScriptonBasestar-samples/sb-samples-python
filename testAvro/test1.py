import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user1.avsc").read())

writer = DataFileWriter(open("dataString1.avro", "w"), DatumWriter(), schema)
writer.append("fewfwefwfwfewfwfwefwefwe")
writer.append("gg34g34g34g34g34g3g43g34g34g43g")
writer.close()

reader = DataFileReader(open("dataString1.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()
