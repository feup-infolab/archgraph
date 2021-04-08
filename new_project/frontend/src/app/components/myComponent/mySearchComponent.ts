export class MySearchComponent {
  public enabledButton: boolean | undefined;
  public fieldsWithValue: number;
  public formOldValue: any;
  public haveResults: boolean;
  public dataSource: any;
  public searchObject: any;

  constructor(
    public mySearchObject: any
  ) {
    console.log(mySearchObject);
    this.searchObject = mySearchObject;
    this.enabledButton = false;
    this.fieldsWithValue = 0;
    this.haveResults = false;
  }

  dataChanged(newObj: any) {
    if (this.formOldValue === '' || this.formOldValue === undefined) {
      if (newObj !== '' || newObj !== undefined) {
        this.fieldsWithValue += 1;
      }
    }
    if (this.formOldValue !== '' || this.formOldValue !== undefined) {
      if (newObj === '' || newObj === undefined) {
        this.fieldsWithValue -= 1;
      }
    }
    console.log(this.fieldsWithValue);
    this.enabledButton = this.fieldsWithValue > 0;
  }

  setHaveResults() {
    this.haveResults = false;
  }
}
