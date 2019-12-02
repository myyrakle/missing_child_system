package com.selab.clidren;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class Move extends AppCompatActivity implements OnMapReadyCallback {
    private GoogleMap mMap;
    EditText editText1;
    Button button;
    int i;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_move);
        button = (Button)findViewById(R.id.button);

        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

    }

    public void onMapReady(final GoogleMap googleMap){
        mMap = googleMap;

        LatLng SEOUL = new LatLng(36.54350854383291, 128.79618668295691);

        MarkerOptions markerOptions = new MarkerOptions();
        markerOptions.position(SEOUL);
        markerOptions.title("안동");
        markerOptions.snippet("안동대학교");
        mMap.addMarker(markerOptions);

        mMap.moveCamera(CameraUpdateFactory.newLatLng(SEOUL));
        mMap.animateCamera(CameraUpdateFactory.zoomTo(10));

    }

    public void btn_Click(View v) {
        mMap.clear();
        EditText editText1 = (EditText) findViewById(R.id.editText1);
        Integer i = Integer.parseInt(editText1.getText().toString());
        onAddMarker(i);
    }
    public void onAddMarker(int i){
        LatLng position = new LatLng(36.54350854383291,128.79618668295691);
        MarkerOptions mymarker = new MarkerOptions().position(position);
        CircleOptions circle = new CircleOptions().center(position).radius(i);
        this.mMap.addMarker(mymarker);
        this.mMap.addCircle(circle);
    }

    public void onClick_back(View v) {
        finish();
    }
}
