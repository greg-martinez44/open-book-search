package Requests;

import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.Request;

public class Post implements RequestInterface {
    public final OkHttpClient client;
    public String url;
    public RequestBody requestBody;
    public final MediaType JSON = MediaType.get("application/json");
    private Request request;

    public Post(String url, String json) {
        this.client = new OkHttpClient();
        this.url = url;
        this.requestBody = RequestBody.create(json, this.JSON);
    }

    public void run() {
        this.request = new Request.Builder()
            .url(this.url)
            .post(this.requestBody)
            .build();
    }

    public Response getResponse() throws IOException {
        Response response = this.client.newCall(this.request).execute();
        if (!response.isSuccessful()) {throw new IOException("Unexpected code: " + response);}
        return response;
    }


}
