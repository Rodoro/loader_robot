package com.example.loader_robot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
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
    private String value;

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
            //TODO: добавить POST к расбери на подключение "connect"
        }
    }

    public void bRecognize(View view) {
        LinearLayout layoutB = findViewById(R.id.buttons);
        LinearLayout layoutT = findViewById(R.id.terminal);

        if(layoutB.getVisibility() == View.VISIBLE) {
            layoutB.setVisibility(View.GONE);
            layoutT.setVisibility(View.VISIBLE);
        } else {
            layoutB.setVisibility(View.VISIBLE);
            layoutT.setVisibility(View.GONE);
        }
    }

    private void post(String post) {
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
                                System.out.println(buffer.toString());
                                value = buffer.toString();
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