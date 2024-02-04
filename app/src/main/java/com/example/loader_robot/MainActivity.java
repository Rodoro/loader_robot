package com.example.loader_robot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Switch;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    private SharedPreferences pref;
    String[] countries = { "Бразилия", "Аргентина", "Колумбия", "Чили", "Уругвай"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        pref = getSharedPreferences("MyPref", MODE_PRIVATE);

        var ip = pref.getString("ip", "");
        if(ip != null) {
            if(ip != "") {
                EditText editText = findViewById(R.id.edAddIp);
                editText.setText(ip);
            }
        }
        postInfo("info");

        ListView countriesList = findViewById(R.id.countriesList);
        ArrayAdapter<String> adapter = new ArrayAdapter(this,
                android.R.layout.simple_list_item_1, countries);
        countriesList.setAdapter(adapter);
    }

    public void bConnect(View view) {
        EditText editText = findViewById(R.id.edAddIp);
        if(editText.getText().toString().equals("")) {
            Toast toast = Toast.makeText(this, "Вы не ввели IP", Toast.LENGTH_LONG);
            toast.show();
        } else {
            var editor = pref.edit();
            editor.putString("ip", editText.getText().toString());
            editor.apply();
            postConnect("connect");
        }
    }

    public void bTurn(View view){
        postTurn("launch");
    }

    public void bRecognize(View view) {
        LinearLayout layoutB = findViewById(R.id.buttons);
        Button button = findViewById(R.id.bOrder);
        LinearLayout layoutT = findViewById(R.id.terminal);

        if(layoutB.getVisibility() == View.VISIBLE) {
            button.setVisibility(View.GONE);
            layoutB.setVisibility(View.GONE);
            layoutT.setVisibility(View.VISIBLE);
        } else {
            button.setVisibility(View.VISIBLE);
            layoutB.setVisibility(View.VISIBLE);
            layoutT.setVisibility(View.GONE);
        }
    }

    public void bOrder(View view) {
        Switch switch1 = findViewById(R.id.bCargo1);
        Switch switch2 = findViewById(R.id.bCargo2);
        Switch switch3 = findViewById(R.id.bCargo3);
        Switch switch4 = findViewById(R.id.bCargo4);
        Switch switch5 = findViewById(R.id.bCargo5);
        Switch switch6 = findViewById(R.id.bCargo6);
        Switch switch7 = findViewById(R.id.bCargo7);
        Switch switch8 = findViewById(R.id.bCargo8);
        Switch switch9 = findViewById(R.id.bCargo9);

        postOrder("order?1=" + Boolean.toString(switch1.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch1.isChecked()).substring(1).toLowerCase() +
                "&2=" + Boolean.toString(switch2.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch2.isChecked()).substring(1).toLowerCase() +
                "&3=" + Boolean.toString(switch3.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch3.isChecked()).substring(1).toLowerCase() +
                "&4=" + Boolean.toString(switch4.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch4.isChecked()).substring(1).toLowerCase() +
                "&5=" + Boolean.toString(switch5.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch5.isChecked()).substring(1).toLowerCase() +
                "&6=" + Boolean.toString(switch6.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch6.isChecked()).substring(1).toLowerCase() +
                "&7=" + Boolean.toString(switch7.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch7.isChecked()).substring(1).toLowerCase() +
                "&8=" + Boolean.toString(switch8.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch8.isChecked()).substring(1).toLowerCase() +
                "&9=" + Boolean.toString(switch9.isChecked()).substring(0,1).toUpperCase() + Boolean.toString(switch9.isChecked()).substring(1).toLowerCase());
    }

    private void postConnect(String post) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    EditText editText = findViewById(R.id.edAddIp);
                    URL url = new URL("http://" + editText.getText().toString() + "/" + post);
                    HttpURLConnection connection = (HttpURLConnection)url.openConnection();
                    if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                        connection.connect();

                        InputStream stream = connection.getInputStream();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));

                        StringBuffer buffer = new StringBuffer();
                        String line = "";

                        while((line = reader.readLine()) != null){
                            buffer.append(line).append("\n");
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String value = buffer.toString();
                                Button button = findViewById(R.id.bConnect);
                                button.setText(value);
                            }
                        });
                    } else {
                        System.out.println(0);
                    }
                } catch(MalformedURLException e){
                    e.printStackTrace();
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void postTurn(String post) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    EditText editText = findViewById(R.id.edAddIp);
                    URL url = new URL("http://" + editText.getText().toString() + "/" + post);
                    HttpURLConnection connection = (HttpURLConnection)url.openConnection();
                    if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                        connection.connect();

                        InputStream stream = connection.getInputStream();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));

                        StringBuffer buffer = new StringBuffer();
                        String line = "";

                        while((line = reader.readLine()) != null){
                            buffer.append(line).append("\n");
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String value = buffer.toString();
                                Button button = findViewById(R.id.bTurn);
                                button.setText(value);
                            }
                        });
                    } else {
                        System.out.println(0);
                    }
                } catch(MalformedURLException e){
                    e.printStackTrace();
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void postInfo(String post) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    EditText editText = findViewById(R.id.edAddIp);
                    URL url = new URL("http://" + editText.getText().toString() + "/" + post);
                    HttpURLConnection connection = (HttpURLConnection)url.openConnection();
                    if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                        connection.connect();

                        InputStream stream = connection.getInputStream();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));

                        StringBuffer buffer = new StringBuffer();
                        String line = "";

                        while((line = reader.readLine()) != null){
                            buffer.append(line).append("\n");//delete it
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String value = buffer.toString();
                                Button button = findViewById(R.id.bTurn);
                                button.setText(value);
                            }
                        });
                    } else {
                        System.out.println(0);
                    }
                } catch(MalformedURLException e){
                    e.printStackTrace();
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void postOrder(String post) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    EditText editText = findViewById(R.id.edAddIp);
                    URL url = new URL("http://" + editText.getText().toString() + "/" + post);
                    HttpURLConnection connection = (HttpURLConnection)url.openConnection();
                    if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                        connection.connect();

                        InputStream stream = connection.getInputStream();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));

                        StringBuffer buffer = new StringBuffer();
                        String line = "";

                        while((line = reader.readLine()) != null){
                            buffer.append(line).append("\n");
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String value = buffer.toString();
                            }
                        });
                    } else {
                        System.out.println(0);
                    }
                } catch(MalformedURLException e){
                    e.printStackTrace();
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}