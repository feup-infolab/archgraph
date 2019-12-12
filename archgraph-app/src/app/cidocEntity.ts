import {CidocRelation} from './cidocRelation'

export class CidocEntity {
	constructor(
		public id: number,
		public name: string,
		public entityType : string,
		public relations: Array<CidocRelation>,
		public dataProperties: Array<CidocRelation>,
		) { }

}