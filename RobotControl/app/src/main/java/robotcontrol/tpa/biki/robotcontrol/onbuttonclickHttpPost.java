package robotcontrol.tpa.biki.robotcontrol;

import android.content.Context;
import android.os.AsyncTask;
import android.os.HandlerThread;
import android.widget.Toast;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class onbuttonclickHttpPost extends AsyncTask<String, Void, String>{
    HandlerThread thread;
    String line, url;
    Context ctx;
    Toast t;

    public onbuttonclickHttpPost(Context ctx)
    {
        this.ctx=ctx;

    }

    @Override
    protected String doInBackground(String... strings) {
        url = strings[0];
        HttpClient httpclient = new DefaultHttpClient();
        HttpGet httppost = new HttpGet(url);
        try {
            HttpResponse response = httpclient.execute(httppost);
            if(url=="http://192.168.43.58/index.php?distance="){
                BufferedReader in = new BufferedReader(new InputStreamReader(
                        response.getEntity().getContent()));
                for(int i = 0; i < 7; i++){
                    line = in.readLine();
                }
            }
        } catch (ClientProtocolException e) {
            // TODO Auto-generated catch block
        } catch (IOException e) {
            // TODO Auto-generated catch block
        }
        return line;
    }

    @Override
    protected void onPostExecute(String result) {
        if(url == "http://192.168.43.58/index.php?distance=") {
           t.makeText(ctx, result, Toast.LENGTH_LONG).show();
        }
        else if (url == "http://192.168.43.58/index.php?shutdown="){
            t.makeText(ctx, "Raspberry Pi Shutdown ", Toast.LENGTH_LONG).show();
        }
        else if (url == "http://192.168.43.58/index.php?reboot="){
            t.makeText(ctx, "Raspberry Pi Rebooted ", Toast.LENGTH_LONG).show();
        }
        else if (url == "http://192.168.43.58/index.php?train="){
            t.makeText(ctx, "Training Started", Toast.LENGTH_LONG).show();
        }
        else if (url == "http://192.168.43.58/index.php?autonomous="){
            t.makeText(ctx, "Autonomous Robot", Toast.LENGTH_LONG).show();
        }
    }
}