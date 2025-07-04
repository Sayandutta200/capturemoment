import boto3
from flask import Flask, jsonify

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name = "ap-south-1")
photographers_table = dynamodb.Table('photographers')
bookings_table = dynamodb.Table('booking')

@app.route('/photographers', methods = ['GET'])
def get_photographers():
    try:
        response = photographers_table.scan()
        return jsonify(response['Items'])
    except Exception as e:
        return jsonify({'error':str(e)}),5000
    
if __name__ == '__main__':
    app.run(debug=True)
