import { Component, Input, Output, EventEmitter } from '@angular/core';
import {CidocEntity} from '../cidocEntity';
import {CidocRelation} from '../cidocRelation'
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http'
import { PipeTransform, Pipe, ViewChild, ViewContainerRef } from '@angular/core';

const httpOptions = {
  	headers: new HttpHeaders({
  		'Content-Type': 'application/json'

  	})
  }

@Component({
  selector: 'app-message',
  template: `<h2>Selected Entity</h2>
  <p>Id: {{myEntity.id}}</p>
   <input type="text" #idInput>
  <button type="submit" (click) = 'changeId(idInput.value)'>Change Id</button>
  <p>Name: {{myEntity.name}}</p>
  <input type="text" #nameInput>
  <button type="submit" (click) = 'changeName(nameInput.value)'>Change Name</button>
  <p>Entity Type {{myEntity.entityType}}</p>
  <div>
  	<button (click)='getRelation(myEntity.entityType)'>Create Relation</button>
  </div>
  <select formControlName="relationControl" #relationS (change)="relationPrep($event.target.value,myEntity.entityType)">
   <option [value]="relation" *ngFor="let relation of possibleRelationsArray"> {{relation}}</option>
 </select>
 <select formControlName="relationControl2" #entityS >
   <option [value]="entity" *ngFor="let entity of possibleCDArray"> {{entity}}</option>
 </select>
 <div>
 	<button (click)='addRelation(relationS.value,entityS.value)'>Add Relation</button>
 </div>
  <div style="height:20px"></div>
  <h2> Property: </h2>
  	<div *ngFor="let property of myEntity.dataProperties">
  		<p>Property Type: {{property.relationType}}</p>
  		<p>Property Value: </p>
  		<div *ngIf=propertyInt(property.destinyType)>
  		<input type="number" formControlName="propertyControl" #propint placeholder= {{property.destinyName}} >
  		<button (click)='changeDataProperty(property.id,propint.value)'> Change Property </button>
  		</div>
  		<div  *ngIf=propertyString(property.destinyType)>
  		<input type="text" #propstring placeholder= {{property.destinyName}}>
  		<button (click)='changeDataProperty(property.id,propstring.value)'> Change Property </button>
  		</div>
  		<div  *ngIf=propertyDate(property.destinyType)>
  		<input type=date #propdate placeholder= {{property.destinyName}}>
  		<button (click)='changeDataProperty(property.id,propdate.value)'> Change Property </button>
  		</div>
  		<div style="height:20px"></div>
  	</div>
  <h2> Relations: </h2>
  	<div *ngFor="let relation of myEntity.relations">
  		<p>Type: {{relation.relationType}}</p>
  		<p>Destination Label: {{relation.destinyName}}</p>
  		<p>Destination Type: {{relation.destinyType}}</p>
  		<a href="#!" (click)="findEntity(relation.id)">Destination Id: {{relation.id}}</a>
  		<div style="height:20px"></div>
  	</div>
  <div>

  </div>
  `,
})

export class MessageComponent{
  @Input() index: number;
  @Input() entityArray: Array<CidocEntity>;
  @Input() json;
  @Input() myEntity: CidocEntity;
  @Input() tableArray: {}[];
  @Output() onJson = new EventEmitter<Object>();
  @Output() onArray = new EventEmitter<Array<CidocEntity>>();
  @Output() onTable = new EventEmitter<{}[]>();



  possibleRelationsArray: String[]=[];
  possibleCDArray: String[]=[];

  constructor(private httpClient: HttpClient){}

  ngOnInit(){
  	console.log(this.myEntity)
  }

  findEntity(xid){
  	console.log(this.index);
  	console.log(this.json);
  	this.myEntity = this.entityArray.find(x => x.id == xid);
  	this.index = this.entityArray.findIndex(x => x.id == xid);
  	console.log(this.index);
  }

  changeJson(){
  	this.json[this.index]["_label"] = "Test"
  	this.entityArray[this.index].name = "Test"
  	this.tableArray[this.index]["Label"] = "Test"
  	this.setJson()
  }

  changeName(val){
  	this.json[this.index]["_label"] = val
  	this.entityArray[this.index].name = val
  	this.tableArray[this.index]["Label"] = val

  	this.setJson()
  }

  changeId(val){
  	this.json[this.index]["@id"] = val
  	this.entityArray[this.index].id = val
  	this.tableArray[this.index]["Id"] = val

  	this.setJson()
  }

  setJson(){
  	this.onJson.emit(this.json)
  	this.onArray.emit(this.entityArray)
  	this.onTable.emit(this.tableArray)
  }

  getRelation(val){
  	this.httpClient.get('http://localhost:5050/cidoc/relations/' + val).subscribe((res)=>{
  		const entries = Object.entries(res)
  		for(const [rel,obj] of entries){
  			this.possibleRelationsArray.push(obj)
  		}
  		console.log(this.possibleRelationsArray)
  	});
  }

  relationPrep(rel,type){
  	console.log(rel)
  	var data = {rel,type, ...this.json}
	console.log(data)
	this.httpClient.post('http://localhost:5050/cidoc/counterdomain',data,httpOptions).subscribe((res)=>{
    		console.log(res);
    		const entries = Object.entries(res)
    		for(const[rel,obj] of entries){
    			this.possibleCDArray.push(obj["@id"])
    		}
    });
  }

  addRelation(rel,ent){
  	console.log(rel)
  	console.log(ent)

  	const entity = this.entityArray.find(x => x.id == ent)
  	const relation: CidocRelation = new CidocRelation(entity.id,rel,entity.name,entity.entityType)
  	this.myEntity.relations.push(relation)

  	this.entityArray[this.index] = this.myEntity

  	if(this.json[this.index][relation.relationType] != null){
  		var addArray: Array<any> =this.json[this.index][relation.relationType]
  		this.json[this.index][relation.relationType].push({
  			"@id" : entity.id,
  			"_label": entity.name,
  			"@type": entity.entityType
  		})
  	}else{
  		this.json[this.index] = {...this.json[this.index], [relation.relationType]:[{
  			"@id" : entity.id,
  			"_label": entity.name,
  			"@type": entity.entityType
  		}]
  	}
  	}



  	this.setJson()
  }


  propertyString(prop){
  	if(prop == "Xsd_String"){
  		return true
  	}else{
  		console.log("test")
  		return false
  	}

  }

  propertyInt(prop){
  	if(prop == "Xsd_Integer"){
  		return true
  	}else{
  		return false
  	}

  }

  propertyDate(prop){
  	if(prop == "Xsd_Date"){
  		return true
  	}else{
  		return false
  	}

  }

  changeDataProperty(id,prop){
  	this.myEntity.dataProperties.find(x => x.id == id).destinyName = prop
  	const entries = Object.entries(this.json)
  	var ind = -1
  	for(const [key, obj] of entries){
  		ind++
  		if(obj["@id"] == id){
  			break
  		}
  	}
  	console.log(ind)
  	console.log(this.index)
  	console.log(prop)
  	this.json[ind]["_label"] = prop
  	this.entityArray[ind].name = prop
  	this.tableArray[ind]["Label"] = prop


  	console.log("before change")
  	console.log(this.json)
  	this.setJson()



  }



}
