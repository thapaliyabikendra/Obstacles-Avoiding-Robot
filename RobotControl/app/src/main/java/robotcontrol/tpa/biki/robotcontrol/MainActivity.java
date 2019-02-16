package robotcontrol.tpa.biki.robotcontrol;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    String url = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button bup=(Button)findViewById(R.id.button7);
        Button bdown=(Button)findViewById(R.id.button13);
        Button bleft=(Button)findViewById(R.id.button12);
        Button bright=(Button)findViewById(R.id.button14);
        Button bdist=(Button)findViewById(R.id.button2);
        Button bcapt=(Button)findViewById(R.id.button);
        Button btrain=(Button)findViewById(R.id.button6);
        Button bauto=(Button)findViewById(R.id.button5);
        Button breboot=(Button)findViewById(R.id.button4);
        Button bshut=(Button)findViewById(R.id.button3);

        bcapt.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?camera=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
                Intent inf=new Intent(MainActivity.this, FSimageView.class);
                startActivity(inf);
            }
        });

        bup.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?up=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bdown.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?down=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bleft.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?left=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bright.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?right=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        breboot.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?reboot=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bshut.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?shutdown=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bauto.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?autonomous=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        btrain.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?train=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });

        bdist.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                url  = "http://192.168.43.58/index.php?distance=";
                new onbuttonclickHttpPost(MainActivity.this).execute(url);
            }
        });
    }
}
