import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Data {
  final List project;
  final List age;
  final List p_name;

  Data({required this.project, required this.age, required this.p_name});

  factory Data.fromJson(Map<String, dynamic> json) {
    return Data(
      project: json['project'] ?? '',
      age: json['age'] ?? '',
      p_name: json['p_name'] ?? '',
    );
  }
}

class DisplayPage extends StatelessWidget {
  final String name;

  DisplayPage({required this.name});

  final myController = TextEditingController();
  String _enteredText = '';

  Future<void> sendDataToFlask(String text) async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:5000/post_data'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'text': text,
      }),
    );
    if (response.statusCode == 200) {
      print('Data sent to Flask server');
    } else {
      print('Failed to send data to Flask server');
    }
  }

  Future<Data> fetchData() async {
    final response = await http.get(Uri.parse('http://127.0.0.1:5000/get_data/${name}'));

    if (response.statusCode == 200) {
      return Data.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to load data');
    }
  }

 @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('Project Recommendation System'),
        ),
        body: Center(
          child: FutureBuilder<Data>(
            future: fetchData(),
            builder: (context, snapshot) {
              if (snapshot.hasData && snapshot.data != null) {
                List<Widget> cards = [];
                for (int i = 0; i < snapshot.data!.project.length; i++) {
                  cards.add(Card(
                    color: Color.fromARGB(255, 208, 204, 204),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                    child: ListTile(
                      leading: Icon(Icons.person),
                      title: Column(
                        children: [
                          SizedBox(height: 10),
                          Text('project-title: ${snapshot.data!.project[i]}'),
                          SizedBox(height: 10),
                          Text('Required Skills:${snapshot.data!.age[i]}'),
                          SizedBox(height: 10),
                          Text('Project Domain:${snapshot.data!.p_name[i]}'),
                        ],
                      ),
                      trailing: Icon(Icons.more_vert),
                    ),
                  ));
                }
                return Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    TextField(
                      textAlignVertical: TextAlignVertical.center,
                      textAlign: TextAlign.left,
                      controller: myController,
                     
                    ),
                    SizedBox(height: 2),
                    Expanded(
                      child: Scrollbar(
                        child: GridView.count(
                          shrinkWrap: true,
                          crossAxisCount: 3,
                          childAspectRatio: 3,
                          children: cards,
                        ),
                      ),
                    ),
                    SizedBox(height: 2),
                  ],
                );
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }
              return CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}