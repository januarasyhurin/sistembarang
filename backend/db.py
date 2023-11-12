import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

firebaseConfig = {
  "apiKey": "AIzaSyDscGiBLPj_biHA_hfzLEZbDUcxi0HQqRY",
  "authDomain": "sistembarang-da89c.firebaseapp.com",
  "databaseURL": "https://sistembarang-da89c-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "sistembarang-da89c",
  "storageBucket": "sistembarang-da89c.appspot.com",
  "messagingSenderId": "655498143663",
  "appId": "1:655498143663:web:132d519fa4caa859fbf15a"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()


def get_all_collection(collection, orderBy=None, direction=None):
    if orderBy:
        collects_ref = db.collection(collection).order_by(
            orderBy, direction=direction)
    else:
        collects_ref = db.collection(collection)
    collects = collects_ref.stream()
    RETURN = []
    for collect in collects:
        ret = collect.to_dict()
        ret['id'] = collect.id
        RETURN.append(ret)
    return RETURN





items = [
    {
        "id": 1,
        "nama_barang": "Samsung J3",
        "merk": "Samsung",
        "kategori": "Smarphone",
        "stok": 2,
        "harga": 10000
    },
    {
        "id": 2,
        "nama_barang": "Apple Iphone 13 ",
        "merk": "Apple",
        "kategori": "Smarphone",
        "stok": 3,
        "harga": 10000
    },
    {
        "id": 3,
        "nama_barang": "JBL Aura",
        "merk": "JBL",
        "kategori": "Speaker",
        "stok": 1,
        "harga": 10000
    },
    {
        "id": 4,
        "nama_barang": "Rexus",
        "merk": "Rexus",
        "kategori": "Keyboard",
        "stok": 1,
        "harga": 10000
    },
    {
        "id": 5,
        "nama_barang": "Kursi Gaming",
        "merk": "Fantech",
        "kategori": "Kursi",
        "stok": 1,
        "harga": 10000
    }
]
