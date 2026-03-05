# UIControlled Application Class

Source: https://www.revitapidocs.com/2026/4638c568-a118-1d57-ceed-a57595202644.htm

---

| UIControlled Application Class |
| --- |

Represents the Autodesk Revit user interface, providing access to
UI customization methods and events. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.UI UIControlledApplication 
  
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm) 
**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class UIControlledApplication
```

```
Public Class UIControlledApplication
```

```
public ref class UIControlledApplication
```

```
type UIControlledApplication = class end
```
The UIControlledApplication type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ActiveAddInId](21e99ede-839f-8230-e399-2b1ae831f643.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ControlledApplication](85b944dc-45d9-e99e-392b-1c720042cd78.htm) | Returns the database level ControlledApplication represented by this UI\-level ControlledApplication. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsLateAddinLoading](05cbbed6-c213-b589-3024-52be90e70ca2.htm) | Indicates whether this add\-in is loaded on the fly or not. If it is loaded when Revit is starting up, it is false, otherwise it should be true. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsViewerModeActive](e5cd8514-02d6-efe1-2172-13b2358bf7fd.htm) | Identifies if the current Revit session is running in Viewer mode |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LoadedApplications](1492b595-f8d9-ff0f-e936-806af51a167d.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MainWindowHandle](a18b37eb-cfa9-198c-bb54-65ca60dd72fa.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ProductIsRS](7ffcb711-729c-229b-063e-6acda6aefeb0.htm) |  |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateAddInCommandBinding](ea28c2a3-378c-146d-ca27-d14145a1d9cf.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateRibbonPanel(String)](9dc43d71-cbe3-d7f5-8086-118f83cb46d8.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateRibbonPanel(String, String)](9d8c0d21-57d3-00c8-ce49-a2323cbce12b.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateRibbonPanel(Tab, String)](8250b04b-f13c-cdd0-fab1-7bad756d746d.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateRibbonTab](8ce17489-75ee-ae81-306d-58f9c505c80c.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDockablePane](71b907a8-c147-3c2e-b2e0-dc268c461e71.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRibbonPanels](f361edc1-cbf2-8334-32c8-dd5492f24435.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRibbonPanels(String)](249b272e-b296-d246-4862-8562270295f0.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRibbonPanels(Tab)](0c912777-d37d-a7e9-390b-622784beba63.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [LoadAddIn](b83c88f3-8861-d89c-fc36-b98b88673782.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [LoadPackageContents](ec42c513-6b6b-b427-1399-8686ad2aa22d.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RegisterContextMenu](f50ebc29-fad5-33a6-3b6e-6d930e7ceee8.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RegisterDockablePane](3c913e04-4444-319e-04bb-61a4784b5d4d.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveAddInCommandBinding](ebf66326-a8e8-cf68-7421-87b12a0eada8.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Events 

|  | Name | Description |
| --- | --- | --- |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ApplicationClosing](98344bdb-5bdd-443a-bb31-ae21ded5fe77.htm) | Subscribe to the ApplicationClosing event to be notified when the Revit application is just about to be closed. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DialogBoxShowing](a5b8870c-d2b8-d3e8-fa35-e9e2166d54f5.htm) | Subscribe to the DialogBoxShowing event to be notified when Revit is just about to show a dialog box or a message box. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DisplayingOptionsDialog](ba28f50d-8545-5e3f-201b-605845c4ed29.htm) | Subscribe to the options dialog displaying event to be notified when Revit options dialog is displaying. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DockableFrameFocusChanged](af99fdfe-6d51-bd56-76b9-756083b1e7d0.htm) | Subscribe to GenericDockableFrame activated event to be notified when Revit GenericDockableFrame is active or inactive. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DockableFrameVisibilityChanged](02c8736f-9f53-80da-5ccc-acf4d1cca406.htm) | Subscribe to GenericDockableFrame showing or hiding event to be notified when Revit GenericDockableFrame is showing or hiding. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FabricationPartBrowserChanged](94e52f48-80d2-979d-bd45-a97d04eaeb8f.htm) | Subscribe to MEP Fabrication part browser changed event to be notified when MEP Fabrication part browser is updated. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FormulaEditing](381fdc01-dd95-22ba-7a8b-c05e3f8de33f.htm) | Subscribe to the FormulaEditing event |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [Idling](e233027b-ba8c-0bd1-37b7-93a066efa5a3.htm) | Subscribe to the Idling event to be notified when Revit is not in an active tool or transaction. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [SelectionChanged](81ada6e8-47f1-4ff6-fcb8-907e0a389c7c.htm) | Subscribe to the SelectionChanged event to be notified after the selection was changed. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ThemeChanged](b363351c-cb5d-f361-fbae-0c3ad37cc4c0.htm) | Subscribe to the ThemeChanged event to be notified after the theme was changed. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [TransferredProjectStandards](82af10d1-5ebf-526d-0dbd-e5ea2270f944.htm) | Subscribe to the TransferredProjectStandards event to be notified after the scope of a Transfer Project Standards operation has been finalized in the Transfer Project Standards dialog. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [TransferringProjectStandards](4c9b9e55-9805-a1ef-bcf9-37687fca3217.htm) | Subscribe to the TransferringProjectStandards event to be notified before the scope of an impending Transfer Project Standards operation has been finalized. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewActivated](583a418b-ea04-bd31-ec88-c262fc1bdb51.htm) | Subscribe to the ViewActivated event to be notified immediately after Revit has finished activating a view of a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewActivating](f217f2ff-6451-d696-dbd2-25603ec76ad6.htm) | Subscribe to the ViewActivating event to be notified when Revit is just about to activate a view of a document. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This class does not provide access to documents because it is provided to you through the ExternalApplication
OnStartup()/OnShutdown() methods, and those methods are when it is not possible to work with Revit documents. 
You can work with documents by getting them from the UIApplication class; that class is obtained from events and 
ExternalCommand callbacks. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)
