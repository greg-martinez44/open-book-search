package Requests;


import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Get implements RequestInterface {
    public final OkHttpClient client;
    public String url;
    private Request request;

    public Get(String url) {
        this.client = new OkHttpClient();
        this.url = url;
    }

    public void run() {
        this.request = new Request.Builder()
            .url(this.url)
            .build();
    }

    public Response getResponse() throws IOException {
        Response response = this.client.newCall(this.request).execute();
        if (!response.isSuccessful()) {throw new IOException("Unexpected code " + response);}
        return response;
    }
}
