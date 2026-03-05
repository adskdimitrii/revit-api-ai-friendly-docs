# Temporary View Modes Class

Source: https://www.revitapidocs.com/2026/cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm

---

| Temporary View Modes Class |
| --- |

A data structure containing data related to temporary view modes. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
Autodesk.Revit.DB TemporaryViewModes 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class TemporaryViewModes : APIObject
```

```
Public Class TemporaryViewModes
	Inherits APIObject
```

```
public ref class TemporaryViewModes : public APIObject
```

```
type TemporaryViewModes = 
    class
        inherit APIObject
    end
```
The TemporaryViewModes type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AcceleratedGraphicsMode](Temporary-View-Modes-Accelerated-Graphics-Mode-Property.md) | The current state of the Accelerated Graphics mode in the associated view. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CustomColor](45773356-1d6a-ad77-1fe3-26d575405f28.htm) | Custom color for the TemporaryViewProperties mode. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CustomTitle](9e59ad90-ea34-b2ee-6893-cd425aadb90f.htm) | Custom title for the TemporaryViewProperties mode. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read\-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](734d88c5-b94f-7ee6-436f-e5d92d4afce8.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [PreviewFamilyVisibility](24f8dd9e-c6e5-7c61-84c6-4556f345e7d4.htm) | The current state of the PreviewFamilyVisibility mode in the associated view. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [PreviewFamilyVisibilityDefaultOnState](295a6ae9-e3c0-795c-d025-fa52b47eea63.htm) | Controls the default state of the PreviewFamilyVisibility mode in all views. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [PreviewFamilyVisibilityDefaultUncutState](1787a21c-c908-637b-46e9-841ac843d840.htm) | Controls the default type of the On state of the PreviewFamilyVisibility mode in cut\-able views. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RevealConstraints](ed674ada-1358-434b-2965-fccd01a3401c.htm) | The current state of the RevealConstraints mode in the associated view. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RevealHiddenElements](87e6bdea-ffa7-fdf1-d190-db9ae56e9bb3.htm) | The current state of the RevealHiddenElements mode in the associated view. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [WorksharingDisplay](86ddd37f-36ef-b63e-559c-ae9a916e89ae.htm) | The current state of the WorksharingDisplay mode in the associated view. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeactivateAllModes](d3ca63c1-b150-c1cd-2610-7083bd1b8263.htm) | Deactivates all temporary modes that are currently active. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeactivateMode](a260a05e-3c58-6d09-901d-a99dfb39186b.htm) | Deactivates the given temporary mode. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCaption](832c859a-4a42-4c2b-8a78-6b15d60f8773.htm) | A text caption to use for the given mode. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCustomized](c7177927-a0b0-0811-675e-87156d8ac40f.htm) | Identifies if a custom temporary view mode is currently active.  A custom mode is active if there is a non\-empty string set for [CustomTitle](9e59ad90-ea34-b2ee-6893-cd425aadb90f.htm) . |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsModeActive](e65c3c3b-2c32-b680-03dd-17ee2318da41.htm) | Tests whether a given mode is currently active or not. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsModeAvailable](c5f8afb6-23aa-1c3f-c637-8cf2e3d09239.htm) | Tests whether a temporary view mode is currently available in the associated view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsModeEnabled](e1b1ad8e-9cee-1969-441d-a8f567874cff.htm) | Tests whether a temporary view mode is currently enabled in the associated view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidState](58a050cd-be15-c5f6-fb03-8bd16462faee.htm) | Tests whether the given state is valid for the associated view and the context the view is currently in. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveCustomization](af568f76-72cd-ee0a-ab1d-b1bd13f2daf2.htm) | Removes all customized values for the TemporaryViewProperties mode. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The class contains methods and properties to manipulate states
 of various temporary view modes that may or may not be avilable
 in any of visible views of a Revit document. The temporary modes are
 enumerated in the [TemporaryViewMode](Temporary-View-Mode-Enumeration.md) class. 

Every view that supports temporary view modes owns an instance
 of this **TemporaryViewModes** class, which can be obtained by
 accessing the [TemporaryViewModes](4828f9cb-4759-2fdb-e842-a592533f6b8c.htm) property of the [View](View-Class.md) class.
 Note that views which do not support temporary modes will have that
 property's value be Null. 

Multiple temporary view modes can coexist.
 Also, TemporaryViewProperties mode can be customized to display custom title and custom color.
 Setting custom title and color affects only TemporaryViewProperties mode for the specific view. 

* [CustomTitle](9e59ad90-ea34-b2ee-6893-cd425aadb90f.htm)
* [CustomColor](45773356-1d6a-ad77-1fe3-26d575405f28.htm)
* [IsCustomized](c7177927-a0b0-0811-675e-87156d8ac40f.htm)
* [RemoveCustomization](af568f76-72cd-ee0a-ab1d-b1bd13f2daf2.htm)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
