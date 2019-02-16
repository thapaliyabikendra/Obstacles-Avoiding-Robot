package robotcontrol.tpa.biki.robotcontrol;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ImageView;
import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.NetworkPolicy;
import com.squareup.picasso.Picasso;

public class FSimageView extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_fsimage_view);
            String MY_URL_STRING = "http://192.168.43.58/image.jpg";
            ImageView ivBasicImage = (ImageView) findViewById(R.id.captureImage);
            Picasso.get().load(MY_URL_STRING).memoryPolicy(MemoryPolicy.NO_CACHE )
                    .networkPolicy(NetworkPolicy.NO_CACHE).into(ivBasicImage);
        }
    }
