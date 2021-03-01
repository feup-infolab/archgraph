package runner;

import org.apache.http.conn.ConnectTimeoutException;
import queries.Queries;
import restservice.RestServiceApplication;
import showcase.Connection;
import showcase.CreateUuids;
import showcase.FillExamples;

import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicLong;

public class Runner {


    private static Connection cn = new Connection();
    private static Queries queries = new Queries();

    public static void main(String args[]) {

        if(cn.getAllBaseUuids().size()==0){
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids.main(null);}
        if(cn.getAllMats().size()==0){
            System.out.println("============================= Filling Data ================================");
            FillExamples.main(null);}
        String[] a = {""};
        RestServiceApplication.main(a);
    }
}
