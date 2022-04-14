interface INode<TElement> {
  data?: TElement
  next?: INode<TElement>
  previous?: INode<TElement>
}

function createEmptyNode<TElement>(): INode<TElement> {
  return { data: undefined, next: undefined, previous: undefined }
}

export class LinkedList<TElement> {
  private head: INode<TElement>
  private tail: INode<TElement>
  private _count: number

  constructor() {
    this._count = 0
    this.head = createEmptyNode()
    this.tail = this.head
  }

  public count(): number {
    return this._count
  }

  public push(element: TElement): void {
    if (this._count === 0) {
      this.head = { data: element }
    } else if (this._count === 1) {
      this.tail = { data: element, previous: this.head }
      this.head.next = this.tail
    } else {
      const newNode = { data: element, previous: this.tail }
      this.tail.next = newNode
      this.tail = newNode
    }
    this._count++
  }

  public unshift(element: TElement): void {
    if (this._count === 0) {
      this.head = { data: element }
    } else {
      const currentHead = this.head
      this.head = { data: element, next: currentHead }
      currentHead.previous = this.head
      this.tail = currentHead
    }
    this._count++
  }

  public pop(): TElement | undefined {
    const lastElement = this.tail.data === undefined ? this.head : this.tail
    const data = lastElement.data
    if (lastElement.previous !== undefined) {
      this.tail = lastElement.previous
    }
    this._count--
    return data
  }

  public shift(): TElement | undefined {
    const currentHead = this.head
    const val = currentHead.data

    if (currentHead.next !== undefined) {
      this.head = currentHead.next
    }

    this._count--
    return val
  }

  public delete(element: TElement): void {
    let node = this.head
    while (node.data !== undefined) {
      if (node.data === element) {
        if (this._count === 1) {
          this.head = createEmptyNode()
          this.tail = this.head
          this._count = 0
          return
        } else if (node.previous) {
          node.previous = node.next
          this._count--
          return
        }
      }
      if (node.next === undefined) {
        break
      }
      node = node.next
    }
  }
}
