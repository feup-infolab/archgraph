package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic


@CompileStatic @Vertex(initSchema = true)
trait E10_Transfer_of_Custody_T implements E7_Activity_T{


    private ArrayList<E39_Actor_T> P28_custody_surrendered_by= new ArrayList<>()


    ArrayList<E39_Actor_T> getP28_custody_surrendered_by() {
        return P28_custody_surrendered_by
    }

    static Object P28_custody_surrendered_by_t = E39_Actor_T.class


    private ArrayList<E39_Actor_T> P29_custody_received_by= new ArrayList<>()


    ArrayList<E39_Actor_T> getP29_custody_received_by() {
        return P29_custody_received_by
    }

    static Object P29_custody_received_by_t = E39_Actor_T.class


    private ArrayList<E18_Physical_Thing_T> P30_transferred_custody_of= new ArrayList<>()


    ArrayList<E18_Physical_Thing_T> getP30_transferred_custody_of() {
        return P30_transferred_custody_of
    }

    static Object P30_transferred_custody_of_t = E18_Physical_Thing_T.class


}