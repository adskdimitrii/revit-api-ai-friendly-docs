# Element Id Class

Source: https://www.revitapidocs.com/2026/44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm

---

| Element Id Class |
| --- |

The ElementId object is used as a unique identification for an element within a
single project. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB ElementId 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ElementId : IComparable
```

```
Public Class ElementId
	Implements IComparable
```

```
public ref class ElementId : IComparable
```

```
type ElementId = 
    class
        interface IComparable
    end
```
The ElementId type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ElementId(BuiltInCategory)](8251e7b1-ea91-ec9c-c8da-6f53a6638811.htm) | Create an ElementId handle with the given BuiltInCategory id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ElementId(BuiltInParameter)](cde49e84-86c6-1fc8-2c50-e5fc6b627470.htm) | Create an ElementId handle with the given BuiltInParameter id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ElementId(Int64\)](0b12e329-90c1-4610-3bae-83df3236266c.htm) | Create an ElementId handle with the given 64\-bit integer id. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [InvalidElementId](08ae8886-6ab3-3ef5-d2e0-0da2ffa7bd2c.htm) | Get the invalid ElementId whose value is \-1\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Value](6f216e39-b66d-5df5-c60c-b9aaccb1e28a.htm) | Provides the value of the element id as a 64\-bit integer. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Compare](697d29f7-4d22-b576-9abc-fbe64803737a.htm) | Compares two element ids. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CompareTo](Element-Id-Compare-To-Method.md) | Compares two element ids. Implementation of System.IComparable interface |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Equals](a5f86bdf-84d9-cc34-7d80-93acf4f5955b.htm) | Determines whether the specified Object is equal to the current Object . (Overrides Object Equals(Object) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHashCode](64b122ce-0c09-ccd4-213d-b06ab6ee7748.htm) | Gets the value of the id as hash code (Overrides Object GetHashCode ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Parse](aa22f1f3-4e78-ebd0-705f-084dd1a54eac.htm) | Parse the string representation of the id into a corresponding ElementId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ToString](db92e345-5a0e-fbad-892a-bea2bd9de941.htm) | Gets a String representation of the value of the id. (Overrides Object ToString ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [TryParse](7b254b04-e251-ea50-3678-4b530009c1b0.htm) | Parse the string representation of the id into a corresponding ElementId. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Operators 

|  | Name | Description |
| --- | --- | --- |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Equality(ElementId, ElementId)](34a21be8-c836-0ac0-fdc8-d45b112ac580.htm) | Determines whether these two ElementIds are the same. |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GreaterThan(ElementId, ElementId)](b6abda7f-8185-14ca-3153-435bf75e56dd.htm) | Determines whether one element id is greater than another element id. |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GreaterThanOrEqual(ElementId, ElementId)](aff18a46-fae0-6048-1eb5-d100240c8dd6.htm) | Determines whether one element id is not less than another element id. |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Inequality(ElementId, ElementId)](8fd25409-ea3f-3bb0-a1cc-6bc7c5895f31.htm) | Determines whether these two ElementIds are different. |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [LessThan(ElementId, ElementId)](be2119ee-e068-3c5f-8bfe-3ac70c6091ea.htm) | Determines whether this element id is less than another element id. |
| ![Public operator](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/puboperator.gif "Public operator")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [LessThanOrEqual(ElementId, ElementId)](ba605698-2cc5-7db5-f07e-33e9b550b9f6.htm) | Determines whether one element id is not greater than another element id. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The Value within the ElementId is only unique with a single project. It is not unique
across several projects. The Id can be used to retrieve a specific element from the database
when needed. However ids are subject to change during an Autodesk Revit session and as such
should not be retained and used across repeated calls to external commands. If a manner is
needed to uniquely identify an element beyond this limitation then a shared parameter should
be added to the element containing a unique identifier managed by the external application. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
