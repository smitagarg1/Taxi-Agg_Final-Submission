import {Id, Location} from './taxi';

export class Customers {
  customerList: Customer[];
}

export class Customer {
  _id: Id;
  name: string;
  location: Location;
  timestamp: Date;
}
