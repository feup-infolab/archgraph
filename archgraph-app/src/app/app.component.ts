import { Component, ViewChild,ViewContainerRef,ComponentFactoryResolver,ComponentRef,ComponentFactory } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MessageComponent } from './message-component/message-component.component';
import {CidocEntity} from './cidocEntity'
import {CidocRelation} from './cidocRelation'
import { HttpHeaders } from '@angular/common/http'
import { PipeTransform, Pipe } from '@angular/core';


const httpOptions = {
  	headers: new HttpHeaders({
  		'Content-Type': 'application/json'

  	})
  }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  objects = [];
  cidocEntities: Array<CidocEntity> = new Array();
  object: string;	
  title = 'archgraph-app';
  type = '';
  componentRef: any;
  st : string;
  items = [{Id:"test",Label:"test2",Type:"test3"}]
  json;

  

  @ViewChild('messagecontainer', {read:ViewContainerRef}) entry: ViewContainerRef;

  constructor(private httpClient: HttpClient, private resolver:ComponentFactoryResolver){ }

  createComponent(index,m2){
  	console.log(this.json)
  	this.entry.clear();
  	const factory = this.resolver.resolveComponentFactory(MessageComponent);
  	const componentRef = this.entry.createComponent(factory);
  	componentRef.instance.index = index;
  	componentRef.instance.entityArray = m2;
  	componentRef.instance.json = this.json;
  	componentRef.instance.myEntity = m2[index];
  	componentRef.instance.tableArray = this.items;
  }


  get_json(){
        this.httpClient.get('http://localhost:5050/cidoc').subscribe((res)=>{
        	this.json = res;
            console.log(res);
            const entries = Object.entries(res)
            this.items.pop()         
            for (const [key, obj] of entries) {
            	this.type = obj["@type"]
            	this.objects.push(obj["_label"])
            	this.objects.push(" ")
            	
            	var relationArray:Array<CidocRelation> = new Array()
            	var propertyArray:Array<CidocRelation> = new Array()
            	

            	for(const p of Object.keys(obj)){
            		if(p.charAt(0) != "P" && p.charAt(0) != "A" ){
            			this.objects.push(p + " : " + obj[p])	
            		}
            		else{
            			this.st = '';
            			for(const o of obj[p]){
            				this.st = this.st + o["_label"] + ';';
            				var regex = new RegExp('^Xsd_.*');
            				if(regex.test(o["@type"])){
            					console.log(o["@type"])
            					propertyArray.push(new CidocRelation(o['@id'],p,o['_label'],o["@type"]))
            					}
            				else{
            					relationArray.push(new CidocRelation(o['@id'],p,o['_label'],o["@type"]))
            					}
            				}
            			this.objects.push(p + " : " + this.st)	
            		}
            		
            	}
            	var entity = new CidocEntity(obj["@id"],obj["_label"],obj["@type"],relationArray,propertyArray)
            	var regex = new RegExp('^Xsd_.*');
            	this.items.push({Id:obj["@id"],Label:obj["_label"],Type:obj["@type"]})
            	this.cidocEntities.push(entity)
            	this.objects.push(" ")
			}
			console.log(this.cidocEntities);
        });
    }

  post_json(){
  		console.log(this.json)
    	this.httpClient.post('http://localhost:5050/cidoc',this.json,httpOptions).subscribe((res)=>{
    		console.log(res);
    	});
    }



  onJson(val: Object) {
  	this.json = val;
  } 

  onArray(val: Array<CidocEntity>){
  	this.cidocEntities = val;
  } 
}




